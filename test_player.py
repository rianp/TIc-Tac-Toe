import unittest
from player import Player, ComputerPlayer


class TestPlayer(unittest.TestCase):

    def test_player(self):
        with self.subTest('has name'):
            player = Player("1", "x")
            expected_output = "1"
            result = player.get_name()
            self.assertEqual(result, expected_output)

        with self.subTest('has mark'):
            player = Player("2", "o")
            expected_output = "o"
            result = player.get_mark()
            self.assertEqual(result, expected_output)


class TestComputerPlayer(unittest.TestCase):
    def setUp(self):
        self.player = ComputerPlayer("1", "x")

    def test_computer_player(self):
        with self.subTest('has name'):
            expected_output = "1"
            result = self.player.get_name()
            self.assertEqual(result, expected_output)

        with self.subTest('has mark'):
            expected_output = "x"
            result = self.player.get_mark()
            self.assertEqual(result, expected_output)

    def test_make_move(self):
        test_cases = [
            {
                "name": "no moves played",
                "board": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                "expected_output": 1
            },
            {
                "name": "one move played",
                "board": [["x", 2, 3], [4, 5, 6], [7, 8, 9]],
                "expected_output": 2
            },
            {
                "name": "two moves played",
                "board": [["x", "o", 3], [4, 5, 6], [7, 8, 9]],
                "expected_output": 3
            },
            {
                "name": "multiple out of order moves played",
                "board": [["x", 2, "o"], ["o", 5, "x"], [7, "x", 9]],
                "expected_output": 2
            },
            {
                "name": "multiple out of order moves played",
                "board": [["x", "x", "o"], ["o", 5, "x"], [7, "x", 9]],
                "expected_output": 5
            },
            {
                "name": "all but one moves played",
                "board": [["x", "o", "x"], ["x", "o", "x"], ["o", "x", 9]],
                "expected_output": 9
            }
        ]

        for test_case in test_cases:
            with self.subTest(test_case["name"]):
                board = test_case["board"]
                expected_output = test_case["expected_output"]

                result = self.player.make_move(board)

                self.assertEqual(result, expected_output)
