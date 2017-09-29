#!/usr/bin/env python
# encoding: utf-8
"""
Tweet a trending topic using shm-reduplication.
"""
from __future__ import print_function, unicode_literals
import argparse
import random
import schpy
import sys
import twitter
import webbrowser
import yaml

from pprint import pprint

HELSINKI_LAT = 60.170833
HELSINKI_LONG = 24.9375

WOE_IDS = {
    # "World": 1,
    # "France": 23424819,
    # "Sweden": 23424954,
    "UK": 23424975,
    "US": 23424977,
}

TWITTER = None


# cmd.exe cannot do Unicode so encode first
def print_it(text):
    print(text.encode('utf-8'))


def load_yaml(filename):
    """
    File should contain:
    consumer_key: TODO_ENTER_YOURS
    consumer_secret: TODO_ENTER_YOURS
    oauth_token: TODO_ENTER_YOURS
    oauth_token_secret: TODO_ENTER_YOURS
    If it contains last_number or last_mention_id, don't change it
    """
    f = open(filename)
    data = yaml.safe_load(f)
    f.close()
    if not data.viewkeys() >= {
            'access_token', 'access_token_secret',
            'consumer_key', 'consumer_secret'}:
        sys.exit("Twitter credentials missing from YAML: " + filename)

    return data


def save_yaml(filename, data):
    with open(filename, 'w') as yaml_file:
        yaml_file.write(yaml.safe_dump(data, default_flow_style=False))


def save_list(the_filename, my_list):
    if args.test:
        return

    with open(the_filename, 'w') as f:
        for s in my_list:
            f.write(s.encode('unicode-escape') + u'\n')


def load_list(the_filename):
    try:
        with open(the_filename, 'r') as f:
            my_list = [
                line.decode('unicode-escape').rstrip(u'\n') for line in f]
    except IOError:
        my_list = []
    return my_list


def case_insensitive_in(a, b):
    """
    Like in(), but case-insensitive.
    case_insensitive_in("x", ["x", "y"]) == True
    case_insensitive_in("X", ["X", "Y"]) == True
    case_insensitive_in("X", ["x", "y"]) == True
    case_insensitive_in("x", ["X", "Y"]) == True
    """
    a_lower = a.lower()
    return any(a_lower == val.lower() for val in b)


def get_trending_topics_from_twitter(location="World"):
    global TWITTER

    print("Location:", location)

    # Create and authorise an app with (read and) write access at:
    # https://dev.twitter.com/apps/new
    # Store credentials in YAML file
    if TWITTER is None:
        TWITTER = twitter.Twitter(auth=twitter.OAuth(
            data['access_token'],
            data['access_token_secret'],
            data['consumer_key'],
            data['consumer_secret']))

    # Returns the locations that Twitter has trending topic information for.
#     world_locations = TWITTER.trends.available()
#     pprint(world_locations)
#     print("*"*80)

    trends = TWITTER.trends.place(_id=WOE_IDS[location])[0]
    pprint(trends)
    print(type(trends))

    kept_trends = []
    for trend in trends['trends']:
        print("-"*80)
        pprint(trend)
        promoted_content = trend['promoted_content']
        trend = trend['name']
        print(trend)
        print("Already posted?", trend in saved_trends)

        if (not trend.lower().endswith("day") and
            not promoted_content and
            not case_insensitive_in(trend, saved_trends)):
            kept_trends.append(trend)

    return kept_trends


def tweet_it(string, in_reply_to_status_id=None):
    global TWITTER

    if len(string) <= 0:
        print("ERROR: trying to tweet an empty tweet!")
        return

    # Create and authorise an app with (read and) write access at:
    # https://dev.twitter.com/apps/new
    # Store credentials in YAML file
    if TWITTER is None:
        TWITTER = twitter.Twitter(auth=twitter.OAuth(
            data['access_token'],
            data['access_token_secret'],
            data['consumer_key'],
            data['consumer_secret']))

    print_it("TWEETING THIS: " + string)

    if args.test:
        print("(Test mode, not actually tweeting)")
    else:
        result = TWITTER.statuses.update(
            status=string,
            # lat=HELSINKI_LAT, long=HELSINKI_LONG,
            display_coordinates=True,
            in_reply_to_status_id=in_reply_to_status_id)
        url = "https://twitter.com/" + \
            result['user']['screen_name'] + "/status/" + result['id_str']
        print("Tweeted: " + url)
        if not args.no_web:
            webbrowser.open(url, new=2)  # 2 = open in a new tab, if possible


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tweet a trending topic using shm-reduplication.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-y', '--yaml',
        default='/Users/hugo/Dropbox/bin/data/schbot.yaml',
        help="YAML file location containing Twitter keys and secrets")
    parser.add_argument(
        '-c', '--cache',
        default='/Users/hugo/Dropbox/bin/data/schbot_trends.txt',
        help="File location containing already posted trends")
    parser.add_argument(
        '-nw', '--no-web', action='store_true',
        help="Don't open a web browser to show the tweeted tweet")
    parser.add_argument(
        '-x', '--test', action='store_true',
        help="Test mode: go through the motions but don't update anything")
    parser.add_argument('-t', '--topic', help="Topic to convert")
    parser.add_argument('-l', '--location', default="random",
                        choices=sorted(WOE_IDS),
                        help="Location of trending topics")
    args = parser.parse_args()

    if args.location == "random":
        args.location = random.choice(WOE_IDS.keys())

    data = load_yaml(args.yaml)
    saved_trends = load_list(args.cache)
    print(saved_trends)

    if args.topic:
        intext = args.topic
        outtext = schpy.topic_schmopic(args.topic)
        print(args.topic)
    else:
        print("Get a topic from Twitter")
        trends = get_trending_topics_from_twitter(args.location)
        pprint(trends)

        if not trends:
            sys.exit("Nowt found, try later")

        for trend in trends:
            intext = trend
            outtext = schpy.topic_schmopic(trend)
            if outtext:
                break
            else:
                sys.exit("no output for " + intext + ", find another")

    if not outtext:
        sys.exit("Nowt found, try later")

    tweet = schpy.print_result(intext, outtext)

    print("Tweet this:\n", tweet)
    try:
        tweet_it(tweet)
        saved_trends.append(intext)
        save_list(args.cache, saved_trends)

    except twitter.api.TwitterHTTPError as e:
        print("*"*80)
        print(e)
        print("*"*80)

# End of file
