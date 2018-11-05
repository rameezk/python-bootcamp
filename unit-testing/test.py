import nose
import unittest
from capitalise import capitalise


class TestCapitalisation(unittest.TestCase):

    def test_single_word(self):
        word = "hello"
        result = capitalise(word)
        self.assertEquals(result, "Hello")

    def test_sentence(self):
        sentence = "hello world"
        result = capitalise(sentence)
        self.assertEquals(result, "Hello World")


if __name__ == "__main__":

    nose.main()
