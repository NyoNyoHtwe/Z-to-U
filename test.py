# -*- coding: utf-8 -*-
import unittest
import zg2uni

class TestZG2UNI(unittest.TestCase):
    def test_article_one(self):
        zawgyi = u'အျပည္ျပည္ဆိုင္ရာ လူ႔အခြင့္အေရး ေၾကျငာစာတမ္း'
        unicode = u'အပြည်ပြည်ဆိုင်ရာ လူ့အခွင့်အရေး ကြေငြာစာတမ်း'
        result = zg2uni.convert(zawgyi)
        self.assertEqual(unicode, result, "Failed converting Article One")

    def test_myanmar_pangram(self):
        zawgyi  = u'ArticleTwo'
        unicode = u'ArticleTwo'
        result = zg2uni.convert(zawgyi)
        self.assertEqual(unicode, result, "Failed converting Myanmar Pangram")

if __name__ == "__main__":
    unittest.main()
