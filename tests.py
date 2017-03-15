import unittest

from tweet import clean_text, customestopwords


class TwitterDataTestCase(unittest.TestCase):
    def test_clean_data(self):
        data = ['gold', 'car', 'jew', 'great', 'http']
        self.assertEqual(clean_text(data), ['gold', 'car', 'jew', 'great',])

if __name__ == '__main__':
    unittest.main()
