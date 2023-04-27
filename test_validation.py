import unittest
from validation import Validator


class TestValidator(unittest.TestCase):

    def setUp(self):
        self.test_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.validator = Validator()

    def test_is_on_board(self):
        test_board = [[1, 2, 3], ['x', 5, 6], [7, 8, 9]]
        with self.subTest('returns true when selection is available'):
            result = self.validator.is_on_board(1, test_board)
            self.assertTrue(result)

        with self.subTest('returns false when selection is not available'):
            result = self.validator.is_on_board(4, test_board)
            self.assertFalse(result)

    def test_is_in_range(self):
        board_range = range(1, len(self.test_board) * len(self.test_board) + 1)
        with self.subTest('returns true when selection is at minimum selection range'):
            result = self.validator.is_in_range(1, board_range)
            self.assertTrue(result)

        with self.subTest('returns true when selection is at maximum selection range'):
            result = self.validator.is_in_range(9, board_range)
            self.assertTrue(result)

        with self.subTest('returns false when selection is lower than selection range'):
            result = self.validator.is_in_range(0, board_range)
            self.assertFalse(result)

        with self.subTest('returns false when selection is higher than selection range'):
            result = self.validator.is_in_range(10, board_range)
            self.assertFalse(result)

    def test_is_valid_integer(self):
        with self.subTest('returns false when input is a character'):
            result = self.validator.is_valid_integer("r")
            self.assertFalse(result)

        with self.subTest('returns false when input is none'):
            result = self.validator.is_valid_integer("")
            self.assertFalse(result)

        with self.subTest('returns false when input is a space'):
            result = self.validator.is_valid_integer(" ")
            self.assertFalse(result)

        with self.subTest('ignores leading whitespace'):
            result = self.validator.is_valid_integer(" 1")
            self.assertTrue(result)

        with self.subTest('ignores trailing whitespace'):
            result = self.validator.is_valid_integer("1 ")
            self.assertTrue(result)

    def test_is_odd(self):
        with self.subTest('returns false when input is an even number'):
            result = self.validator.is_odd(2)
            self.assertFalse(result)

    def test_validate_size(self):
        with self.subTest(
                "should notify player their result is invalid if they entered a non-integer"
        ):
            size = "cookie"
            self.validator.is_valid_integer.return_value = False

            result = self.validator.validate_size(size)

            self.assertEqual(result.is_valid, False)
            self.assertEqual(result.message, "Eek! That's not even a number! ")

        with self.subTest(
                "should notify player of out-of-range size if board size is out of selectable range"
        ):
            size = "10"
            self.validator.is_valid_integer.return_value = True
            self.validator.is_in_range.return_value = False

            result = self.validator.validate_size(size)

            self.assertEqual(result.is_valid, False)
            self.assertEqual(result.message, "Whoa friend! This is outta bounds! ")

        with self.subTest(
                "should notify player result is invalid if chosen size is even"
        ):
            size = "4"
            self.validator.is_valid_integer.return_value = True
            self.validator.is_in_range.return_value = True
            self.validator.is_odd.return_value = False

            result = self.validator.validate_size(size)

            self.assertEqual(result.is_valid, False)
            self.assertEqual(result.message, "Ummm. This isn't odd friend!")

        with self.subTest(
                "should indicate result is valid if chosen size is a valid odd integer"
        ):
            size = "3"
            self.validator.is_valid_integer.return_value = True
            self.validator.is_in_range.return_value = True
            self.validator.is_odd.return_value = True

            result = self.validator.validate_size(size)

            self.assertEqual(result.is_valid, True)
            self.assertEqual(result.message, "")

    def test_validate_choice(self):
        with self.subTest(
                "should notify player their result is invalid if they entered a non-integer"
        ):
            size = "cookie"
            self.validator.is_valid_integer.return_value = False

            result = self.validator.validate_choice(size)

            self.assertEqual(result.is_valid, False)
            self.assertEqual(result.message, "Eek! That's not even a number! ")

        with self.subTest(
                "should notify player of out-of-range choice if opponent choice is out of selectable range"
        ):
            size = "3"
            self.validator.is_valid_integer.return_value = True
            self.validator.is_in_range.return_value = False

            result = self.validator.validate_choice(size)

            self.assertEqual(result.is_valid, False)
            self.assertEqual(result.message, "Whoa friend! This is outta bounds! ")

        with self.subTest(
                "should indicate result is valid if chosen opponent is a valid choice"
        ):
            size = "2"
            self.validator.is_valid_integer.return_value = True
            self.validator.is_in_range.return_value = True
            self.validator.is_odd.return_value = True

            result = self.validator.validate_choice(size)

            self.assertEqual(result.is_valid, True)
            self.assertEqual(result.message, "")
