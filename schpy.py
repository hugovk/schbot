#!/usr/bin/env python
# encoding: utf-8
"""
Output some text using shm-reduplication.
https://en.wikipedia.org/wiki/Shm-reduplication
https://www.academia.edu/209796/Metalinguistic_shmetalinguistic_The_phonology_of_shm-reduplication
"""
from __future__ import print_function, unicode_literals
import argparse
import random


CONSONANTS = "bcdfghjklmnpqrstvwxyz"
TERMINATORS = ["!", "..."]


def is_vowel(char, i=0):
    """
    Assumptions:
     * Y at the start of a word is not a vowel.
     * Y anywhere else is a vowel.
    """
    if i == 0:
        return char.lower() not in CONSONANTS
    else:
        if char.lower() == 'y':
            return True
        else:
            return char.lower() not in CONSONANTS


def first_vowel(word):
    """Return index of first vowel"""
    for i in range(len(word)):
        if is_vowel(word[i], i):
            return i
    return -1


def startswith_consonants(word, final_consonant_in_cluster=False):
    """
    Does the word begin with a consonant cluster?
    Does the consonant cluster end with a char in string
    final_consonant_in_cluster? (e.g. "rl")
    e.g. breakfast, street, floozie
    """
    if is_vowel(word[0]):
        return False
    else:
        v_pos = first_vowel(word)
        if final_consonant_in_cluster:
            if word[v_pos - 1] in final_consonant_in_cluster:
                return True
        else:
            return True

    return False


def schpy(phrase):
    words = phrase.split()
    if not words:
        return ""
    last_word = words[-1].lower()

    if last_word.startswith("schm"):
        last_word = "schn" + last_word[4:]
    elif last_word.startswith("schn"):
        last_word = "schm" + last_word[4:]
    elif last_word.startswith("sm"):
        last_word = "schm" + last_word[2:]
    elif last_word.startswith("sn"):
        last_word = "schm" + last_word[2:]
    elif last_word.startswith("qu"):
        last_word = "schm" + last_word[2:]
    elif(startswith_consonants(last_word, "rlk")):
        v_pos = first_vowel(last_word)
        last_word = "schm" + last_word[v_pos:]
#     elif last_word[0] in CONSONANTS and last_word[1] in CONSONANTS:
#         last_word = "schm" + last_word[1:]
    # CONSONANT-VOWEL-
    elif (last_word[0] in CONSONANTS and
          last_word[1] not in CONSONANTS):
        last_word = "schm" + last_word[1:]
    # CONSONANT-CONSONANT-VOWEL-
    elif (last_word[0] in CONSONANTS and
          last_word[1] in CONSONANTS and
          last_word[2] not in CONSONANTS):
        last_word = "schm" + last_word[2:]
    elif last_word[0] not in CONSONANTS:
        last_word = "schm" + last_word
    else:
        # schm-[FIRST-VOWEL]-
        v_pos = first_vowel(last_word)
        last_word = "schm" + last_word[v_pos:]

    # ALL CAPS
    if words[-1].isupper():
        last_word = last_word.upper()
    # Initial Caps
    elif words[-1].istitle():
        last_word = last_word.title()

    words = words[:-1] + [last_word]
    return " ".join(words)


def camel_case_to_spaced(string):
    """
    Split string by upper case letters.
    @return words (list)
    """
    words = []
    new_word_pos = 0
    for i, c in enumerate(string):
        if c.isupper() and new_word_pos < i:
            words.append(string[new_word_pos:i])
            new_word_pos = i
    words.append(string[new_word_pos:])
    print(words)
    return " ".join(words)


def topic_schmopic(topic):
    """
    Split a phrase into words. Hashtags may be camel case.
    """
    hashtag = False
    if topic[0] == "#":
        hashtag = True
        topic = topic[1:]

    # Skip things that end in numbers (e.g. Uncharted 4)
    splitted = topic.split()
    try:
        int(splitted[-1])
        return False
    except ValueError:
        pass

    if " " in topic:
        words = schpy(topic)
    elif topic.isupper():  # "ABC123" also True
        words = schpy(topic)
    else:
        words = schpy(camel_case_to_spaced(topic))
        words = words.replace(" ", "")

    if hashtag:
        words = "#" + words

    return words


def print_result(intext, outtext):
    text = intext + "? " + outtext + random.choice(TERMINATORS)
    print(text)
    return text


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Output some text using shm-reduplication.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-p', '--phrase', help="Phrase to convert")
    parser.add_argument('-t', '--topic',
                        help="Twitter trending topic to convert")
    args = parser.parse_args()

    if args.phrase:
        intext = args.phrase
        outtext = schpy(args.phrase)
    elif args.topic:
        intext = args.topic
        outtext = topic_schmopic(args.topic)

    print_result(intext, outtext)

# End of file
