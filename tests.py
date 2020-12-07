import unittest
from app import word_occurence

import tempfile, os
tmp = tempfile.NamedTemporaryFile()

def tempfilesetup(testdata):
    t = tempfile.NamedTemporaryFile(mode='w',dir="./",delete=False)
    t.write(testdata)
    t.close()
    os.chmod(t.name, 0o777)
    return t.name

class TestSum(unittest.TestCase):

    def test_wordcount(self):
        test_data = "This sentence contains ten words from start till the end."
        testfile = tempfilesetup(test_data)       
        wordcount = word_occurence(testfile)

        os.unlink(testfile)
        self.assertEqual(wordcount[0], 10)

    def test_punctuation(self):
        test_data = "This is a check for words with punctuations; This check helps A, B and C!"
        testfile = tempfilesetup(test_data)       
        wordcount = word_occurence(testfile)

        os.unlink(testfile)
        self.assertEqual(wordcount[0], 15, 15)

    def test_wild_characters(self):
        test_data = "This is a check for words~` with #wild characters#; %This check helps A` B` and C`!"
        testfile = tempfilesetup(test_data)       
        wordcount = word_occurence(testfile)

        os.unlink(testfile)
        self.assertEqual(wordcount[0], 16, "Word count does not match")

    def test_numbers(self):
        test_data = "1 2 3 4 5 6 7 8 9 10"
        testfile = tempfilesetup(test_data)       
        wordcount = word_occurence(testfile)

        os.unlink(testfile)
        self.assertEqual(wordcount[0], 10, "Word count does not match")

    
    def test_empty_file(self):
        test_data = ""
        testfile = tempfilesetup(test_data)       
        wordcount = word_occurence(testfile)

        os.unlink(testfile)
        self.assertEqual(wordcount, 'Empty file, no words found.')
    
    def test_zero_word_count(self):
        test_data = "      "
        testfile = tempfilesetup(test_data)       
        wordcount = word_occurence(testfile)

        os.unlink(testfile)
        self.assertEqual(wordcount, 'File contains only spaces, no words')
    
    
    def test_missing_file(self):
        test_data = "This is a check for incorrect/missing file"
        testfile = "Incorrectfile"       
        wordcount = word_occurence(testfile)

        self.assertEqual(wordcount, 'File not found')
    

if __name__ == '__main__':
    unittest.main()