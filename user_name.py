import re
import unittest


def validate(username):
    """validates a username based on the following rules:
     - Atleast four character
     - Starts with a letter
     - Ends with a letter or number
     - Contains only letters and numbers, and optionally up to one underscore

    Args:
    username -- (string) the proposed username to check

    Returns:
    (bool) True if the username is acceptable, otherwise False
    """
    reg_string = r"^[a-zA-Z][\w]{2,}[a-zA-Z0-9]$"  # nopep8
    return bool(re.match(reg_string, username)) and (username.count("_") < 2)


class TestValidate(unittest.TestCase):

    def test_middle_underscore(self):
        res = validate("a_aa")
        self.assertEqual(res, True)

    def test_end_underscore(self):
        res = validate("aaaa_")
        self.assertEqual(res, False)

    def test_beginning_underscore(self):
        res = validate("_aaaaa")
        self.assertEqual(res, False)

    def test_three_cha(self):
        res = validate("aaa")
        self.assertEqual(res, False)

    def test_non_alphanum(self):
        res = validate("aa%aa")
        self.assertEqual(res, False)

    def test_all_alpha(self):
        res = validate("aaaaa")
        self.assertEqual(res, True)

    def test_beginning_number(self):
        res = validate("0aaaaa")
        self.assertEqual(res, False)

    def test_end_underscore(self):
        res = validate("aaaaa_")
        self.assertEqual(res, False)

    def test_empty_string(self):
        res = validate("")
        self.assertEqual(res, False)

    def test_two_underscores(self):
        res = validate("aaa_aa_b")
        self.assertEqual(res, False)


if __name__ == '__main__':
    unittest.main()
