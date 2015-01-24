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
        intext = "table"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmable")

    def test_start_single_consonant2(self):
        intext = "HOTEL"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "SCHMOTEL")

    def test_start_consonant_cluster1(self):
        """
        Words beginning with a consonant cluster are more variable:
        some speakers replace only the first consonant if possible
        (breakfast shmreakfast), others replace the entire cluster
        (breakfast shmeakfast).
        """
        intext = "breakfast"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmeakfast")

    def test_start_consonant_cluster2(self):
        intext = "group"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmoup")

    def test_start_vowel1(self):
        """
        Vowel-initial words prepend the shm- directly to the beginning of the
        reduplicant (apple shmapple).
        """
        intext = "apple"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmapple")

    def test_two_words1(self):
        """
        When speaking two words, usually only the second word is
        shm-reduplicated (Led Zeppelin Led Shmeppelin).
        """
        intext = "Led Zeppelin"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "Led Schmeppelin")

    def test_three_words1(self):
        """
        """
        intext = "red and yellow"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "red and schmellow")

    def test_schm_words1(self):
        """
        Shm-reduplication is generally avoided or altered with words that
        already begin with shm-; for instance, schmuck does not yield the
        expected *schmuck schmuck, but rather total avoidance or mutation of
         the shm- (giving forms like schmuck shluck, schmuck fluck, and so on).
        """
        intext = "schmuck"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schnuck")

    def test_bagel(self):
        intext = "bagel"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmagel")

    def test_accent(self):
        intext = "Joe"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "Schmoe")

    def test_money(self):
        intext = "money"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmoney")

    def test_father(self):
        intext = "father"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmather")

    def test_page(self):
        intext = "page"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmage")

    def test_crisis(self):
        intext = "crisis"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmisis")

    def test_street(self):
        intext = "street"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmeet")

    def test_rich(self):
        intext = "rich"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmich")

    def test_floozie(self):
        intext = "floozie"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmoozie")

    def test_floss(self):
        intext = "floss"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmoss")

    def test_broom(self):
        intext = "broom"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmoom")

    def test_first_vowel_found(self):
        intext = "bad"
        outtext = schpy.first_vowel(intext)
        self.assertEqual(outtext, 1)

    def test_first_vowel_not_found(self):
        intext = "bd"
        outtext = schpy.first_vowel(intext)
        self.assertEqual(outtext, -1)

    def test_union(self):
        intext = "union"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmunion")

    def test_wig(self):
        intext = "wig"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmig")

    def test_nothing(self):
        intext = ""
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "")

    def test_witches(self):
        intext = "witches"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmitches")

    def test_ashmont(self):
        intext = "Ashmont"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "Schmashmont")

    def test_ishmael(self):
        intext = "Ishmael"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "Schmishmael")

    def test_ash(self):
        intext = "ash"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmash")

    def test_gibberish(self):
        intext = "gibberish"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmibberish")

    def test_massage(self):
        intext = "massage"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmassage")

    def test_circus(self):
        intext = "circus"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmircus")

    def test_schnozz(self):
        intext = "schnozz"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmozz")

    def test_terrific(self):
        intext = "terrific"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmerrific")

    def test_obscene(self):
        intext = "obscene"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmobscene")

    def test_walkman(self):
        intext = "walkman"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmalkman")

    def test_schmidt(self):
        intext = "Schmidt"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "Schnidt")

    def test_schmooze(self):
        intext = "schmooze"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schnooze")

    def test_metalinguistic(self):
        intext = "metalinguistic"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmetalinguistic")

    def test_sky(self):
        intext = "sky"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmy")

    def test_topic_schmopic_1(self):
        intext = "Until Dawn"
        outtext = schpy.topic_schmopic(intext)
        self.assertEqual(outtext, "Until Schmawn")

    def test_topic_schmopic_2(self):
        intext = "#CameronMustGo"
        outtext = schpy.topic_schmopic(intext)
        self.assertEqual(outtext, "#CameronMustSchmo")

    def test_topic_schmopic_3(self):
        intext = "Uncharted 4"
        outtext = schpy.topic_schmopic(intext)
        self.assertEqual(outtext, False)

    def test_topic_schmopic_4(self):
        intext = "#hayesvideo"
        outtext = schpy.topic_schmopic(intext)
        self.assertEqual(outtext, "#schmayesvideo")

    def test_topic_schmopic_5(self):
        intext = "#100kHappyBailey"
        outtext = schpy.topic_schmopic(intext)
        self.assertEqual(outtext, "#100kHappySchmailey")

    def test_topic_schmopic_6(self):
        intext = "#XFactorSemiFinal"
        outtext = schpy.topic_schmopic(intext)
        self.assertEqual(outtext, "#XFactorSemiSchminal")

    def test_topic_schmopic_7(self):
        intext = "#PlayStationExperience"
        outtext = schpy.topic_schmopic(intext)
        self.assertEqual(outtext, "#PlayStationSchmexperience")

    def test_topic_schmopic_8(self):
        intext = "No Man's Sky"
        outtext = schpy.topic_schmopic(intext)
        self.assertEqual(outtext, "No Man's Schmy")

    def test_topic_schmopic_9(self):
        intext = "Mariah"
        outtext = schpy.topic_schmopic(intext)
        self.assertEqual(outtext, "Schmariah")

    def test_topic_schmopic_10(self):
        intext = "Yakuza 5"
        outtext = schpy.topic_schmopic(intext)
        self.assertEqual(outtext, False)

    def test_sniper(self):
        intext = "sniper"
        outtext = schpy.topic_schmopic(intext)
        self.assertEqual(outtext, "schmiper")

    def test_smart(self):
        intext = "smart"
        outtext = schpy.topic_schmopic(intext)
        self.assertEqual(outtext, "schmart")

    def test_topic_schmopic_11(self):
        intext = "American Sniper"
        outtext = schpy.topic_schmopic(intext)
        self.assertEqual(outtext, "American Schmiper")

    def test_topic_schmopic_12(self):
        intext = "FINTECH2015"
        outtext = schpy.topic_schmopic(intext)
        self.assertEqual(outtext, "SCHMINTECH2015")

    def test_quotes(self):
        intext = "quotes"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmotes")

    def test_topic_schmopic_13(self):
        intext = "#SnotQuotes"
        outtext = schpy.topic_schmopic(intext)
        self.assertEqual(outtext, "#SnotSchmotes")

    def test_print_result(self):
        in_intext = "bot"
        in_outtext = "schmot"
        out_outtext = schpy.print_result(in_intext, in_outtext)
        self.assertIn("bot? schmot", out_outtext)

    def test_this(self):
        intext = "this"
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schmis")

#     def test_topic_schmopic_11(self):
#         intext = "#MCFCvEFC"
#         outtext = schpy.topic_schmopic(intext)
#         self.assertEqual(outtext, "#MCFCvEFC")

    def xtest_(self):
        intext = ""
        outtext = schpy.schpy(intext)
        self.assertEqual(outtext, "schm")


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
