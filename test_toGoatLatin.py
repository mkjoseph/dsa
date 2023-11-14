import unittest
from toGoatLatin import toGoatLatin

class TestToGoatLatin(unittest.TestCase):
    def test_toGoatLatin(self):
        self.assertEqual(toGoatLatin("I speak Goat Latin"), "Imaa peaksmaaa oatGmaaaa atinLmaaaaa")
        self.assertEqual(toGoatLatin("The quick brown fox jumped over the lazy dog"), "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa")
        self.assertEqual(toGoatLatin("Hello World"), "elloHmaa orldWmaaa")
        self.assertEqual(toGoatLatin("Python is awesome"), "ythonPmaa ismaaa wesomeamaaa")
        self.assertEqual(toGoatLatin("a"), "amaa")
        self.assertEqual(toGoatLatin("A"), "amaa")

if __name__ == '__main__':
    unittest.main()