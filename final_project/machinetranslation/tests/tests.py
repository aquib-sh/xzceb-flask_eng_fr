import unittest
from translator import LanguageTranslator

class TestE2F(unittest.TestCase):
    def test_null(self):
        translator = LanguageTranslator()
        text = None
        expected = None
        translation = translator.englishToFrench(text)
        self.assertTrue(translation, expected)

    def test_str(self):
        translator = LanguageTranslator()
        text = "Hello"
        expected = "Bonjour"
        translation = translator.englishToFrench(text)
        self.assertTrue(translation, expected)

class TestF2E(unittest.TestCase):
    def test_null(self):
        translator = LanguageTranslator()
        text = None
        expected = None
        translation = translator.frenchToEnglish(text)
        self.assertTrue(translation, expected)

    def test_str(self):
        translator = LanguageTranslator()
        text = "Bonjour"
        expected = "Hello"
        translation = translator.frenchToEnglish(text)
        self.assertTrue(translation, expected)

if __name__ == "__main__":
    unittest.main()