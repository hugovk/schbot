#!/usr/bin/env python
# encoding: utf-8
"""
Unit tests for schpy.py
https://en.wikipedia.org/wiki/Shm-reduplication
http://www.academia.edu/209796/Metalinguistic_shmetalinguistic_The_phonology_of_shm-reduplication
"""
from __future__ import print_function, unicode_literals
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import schpy


class TestIt(unittest.TestCase):

    def test_start_single_consonant1(self):
        """
        Words beginning with a single consonant typically replace that
        consonant with shm- (table shmable).
        """
        input = "table"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmable")

    def test_start_single_consonant2(self):
        input = "HOTEL"
        output = schpy.schpy(input)
        self.assertEqual(output, "SCHMOTEL")

    def test_start_consonant_cluster1(self):
        """
        Words beginning with a consonant cluster are more variable:
        some speakers replace only the first consonant if possible
        (breakfast shmreakfast), others replace the entire cluster
        (breakfast shmeakfast).
        """
        input = "breakfast"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmeakfast")

    def test_start_consonant_cluster2(self):
        input = "group"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmoup")

    def test_start_vowel1(self):
        """
        Vowel-initial words prepend the shm- directly to the beginning of the
        reduplicant (apple shmapple).
        """
        input = "apple"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmapple")

    def test_two_words1(self):
        """
        When speaking two words, usually only the second word is
        shm-reduplicated (Led Zeppelin Led Shmeppelin).
        """
        input = "Led Zeppelin"
        output = schpy.schpy(input)
        self.assertEqual(output, "Led Schmeppelin")

    def test_three_words1(self):
        """
        """
        input = "red and yellow"
        output = schpy.schpy(input)
        self.assertEqual(output, "red and schmellow")

    def test_schm_words1(self):
        """
        Shm-reduplication is generally avoided or altered with words that
        already begin with shm-; for instance, schmuck does not yield the
        expected *schmuck schmuck, but rather total avoidance or mutation of
         the shm- (giving forms like schmuck shluck, schmuck fluck, and so on).
        """
        input = "schmuck"
        output = schpy.schpy(input)
        self.assertEqual(output, "schnuck")

    def test_bagel(self):
        input = "bagel"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmagel")

    def test_accent(self):
        input = "Joe"
        output = schpy.schpy(input)
        self.assertEqual(output, "Schmoe")

    def test_money(self):
        input = "money"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmoney")

    def test_father(self):
        input = "father"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmather")

    def test_page(self):
        input = "page"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmage")

    def test_crisis(self):
        input = "crisis"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmisis")

    def test_street(self):
        input = "street"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmeet")

    def test_rich(self):
        input = "rich"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmich")

    def test_floozie(self):
        input = "floozie"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmoozie")

    def test_floss(self):
        input = "floss"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmoss")

    def test_broom(self):
        input = "broom"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmoom")

    def test_first_vowel_found(self):
        input = "bad"
        output = schpy.first_vowel(input)
        self.assertEqual(output, 1)

    def test_first_vowel_not_found(self):
        input = "bd"
        output = schpy.first_vowel(input)
        self.assertEqual(output, -1)

    def test_union(self):
        input = "union"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmunion")

    def test_wig(self):
        input = "wig"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmig")

    def test_nothing(self):
        input = ""
        output = schpy.schpy(input)
        self.assertEqual(output, "")

    def test_witches(self):
        input = "witches"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmitches")

    def test_ashmont(self):
        input = "Ashmont"
        output = schpy.schpy(input)
        self.assertEqual(output, "Schmashmont")

    def test_ishmael(self):
        input = "Ishmael"
        output = schpy.schpy(input)
        self.assertEqual(output, "Schmishmael")

    def test_ash(self):
        input = "ash"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmash")

    def test_gibberish(self):
        input = "gibberish"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmibberish")

    def test_massage(self):
        input = "massage"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmassage")

    def test_circus(self):
        input = "circus"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmircus")

    def test_schnozz(self):
        input = "schnozz"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmozz")

    def test_terrific(self):
        input = "terrific"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmerrific")

    def test_obscene(self):
        input = "obscene"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmobscene")

    def test_walkman(self):
        input = "walkman"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmalkman")

    def test_schmidt(self):
        input = "Schmidt"
        output = schpy.schpy(input)
        self.assertEqual(output, "Schnidt")

    def test_schmooze(self):
        input = "schmooze"
        output = schpy.schpy(input)
        self.assertEqual(output, "schnooze")

    def test_metalinguistic(self):
        input = "metalinguistic"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmetalinguistic")

    def test_sky(self):
        input = "sky"
        output = schpy.schpy(input)
        self.assertEqual(output, "schmy")

    def test_topic_schmopic_1(self):
        input = "Until Dawn"
        output = schpy.topic_schmopic(input)
        self.assertEqual(output, "Until Schmawn")

    def test_topic_schmopic_2(self):
        input = "#CameronMustGo"
        output = schpy.topic_schmopic(input)
        self.assertEqual(output, "#CameronMustSchmo")

    def test_topic_schmopic_3(self):
        input = "Uncharted 4"
        output = schpy.topic_schmopic(input)
        self.assertEqual(output, False)

    def test_topic_schmopic_4(self):
        input = "#hayesvideo"
        output = schpy.topic_schmopic(input)
        self.assertEqual(output, "#schmayesvideo")

    def test_topic_schmopic_5(self):
        input = "#100kHappyBailey"
        output = schpy.topic_schmopic(input)
        self.assertEqual(output, "#100kHappySchmailey")

    def test_topic_schmopic_6(self):
        input = "#XFactorSemiFinal"
        output = schpy.topic_schmopic(input)
        self.assertEqual(output, "#XFactorSemiSchminal")

    def test_topic_schmopic_7(self):
        input = "#PlayStationExperience"
        output = schpy.topic_schmopic(input)
        self.assertEqual(output, "#PlayStationSchmexperience")

    def test_topic_schmopic_8(self):
        input = "No Man's Sky"
        output = schpy.topic_schmopic(input)
        self.assertEqual(output, "No Man's Schmy")

    def test_topic_schmopic_9(self):
        input = "Mariah"
        output = schpy.topic_schmopic(input)
        self.assertEqual(output, "Schmariah")

    def test_topic_schmopic_10(self):
        input = "Yakuza 5"
        output = schpy.topic_schmopic(input)
        self.assertEqual(output, False)

    def test_sniper(self):
        input = "sniper"
        output = schpy.topic_schmopic(input)
        self.assertEqual(output, "schmiper")

    def test_smart(self):
        input = "smart"
        output = schpy.topic_schmopic(input)
        self.assertEqual(output, "schmart")

    def test_topic_schmopic_11(self):
        input = "American Sniper"
        output = schpy.topic_schmopic(input)
        self.assertEqual(output, "American Schmiper")

    def test_topic_schmopic_12(self):
        input = "FINTECH2015"
        output = schpy.topic_schmopic(input)
        self.assertEqual(output, "SCHMINTECH2015")

    def test_quotes(self):
        input = "quotes"
        output = schpy.topic_schmopic(input)
        self.assertEqual(output, "schmotes")

    def test_topic_schmopic_13(self):
        input = "#SnotQuotes"
        output = schpy.topic_schmopic(input)
        self.assertEqual(output, "#SnotSchmotes")

#     def test_topic_schmopic_11(self):
#         input = "#MCFCvEFC"
#         output = schpy.topic_schmopic(input)
#         self.assertEqual(output, "#MCFCvEFC")

    def xtest_(self):
        input = ""
        output = schpy.schpy(input)
        self.assertEqual(output, "schm")


# Some speakers target the stressed syllable rather than the first syllable
# (incredible inshmedible); a subset of these do not copy base material
# preceding the stressed syllable (incredible shmedible; cf. Spitzer 1952).
# Many speakers use sm- instead of shm- with words that contain a sh (Ashmont
# Smashmont, not *shmashmont).

# TODO caps
# TODO schm vs shm option

if __name__ == '__main__':
    unittest.main()

# End of file
