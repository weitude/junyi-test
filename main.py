def reverse_string(string):
    return string[::-1]


def reverse_every_vocab(string):
    ans = []
    split_string = string.split(" ")
    for s in split_string:
        ans.append(reverse_string(s))
    return " ".join(ans)


# Question A
string = "test"
print("Question A:")
print("Original string:", string)
print("Reversed string:", reverse_string(string))
print()

# Question B
string = "this is a test string"
print("Question B:")
print("Original string:", string)
print("Reversed string:", reverse_every_vocab(string))
print()

# Question C

import unittest


class TestReverseString(unittest.TestCase):
    def test_question_a(self):
        self.assertEqual(reverse_string('hello'), 'olleh')
        self.assertEqual(reverse_string('123456789'), '987654321')
        self.assertEqual(reverse_string(''), '')
        self.assertEqual(reverse_string('a'), 'a')
        self.assertEqual(reverse_string('racecar'), 'racecar')

    def test_question_b(self):
        self.assertEqual(reverse_every_vocab('junyi is wonderful'), 'iynuj si lufrednow')
        self.assertEqual(reverse_every_vocab('a b c'), 'a b c')
        self.assertEqual(reverse_every_vocab(''), '')


if __name__ == '__main__':
    unittest.main()
