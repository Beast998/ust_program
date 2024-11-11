import unittest
from src.word_count import compute_word_frequency
from src.read import read_input_file

class TestWordFrequency(unittest.TestCase):

    def test_compute_word_frequency(self):
        text = "which is better python 2 or python 3"
        expected_output = [('2', 1), ('3', 1), ('better', 1), ('is', 1), ('or', 1), ('python', 2), ('which', 1)]
        self.assertEqual(compute_word_frequency(text), expected_output)

    def test_read_input_file(self):
        test_filename = 'C:\\Users\\Admin\\PycharmProjects\\word_counter\\input_data\\input.txt'
        with open(test_filename, 'w') as file:
            file.write("test input file content")

        self.assertEqual(read_input_file(test_filename), "test input file content")

if __name__ == '__main__':
    unittest.main()
