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
        with self.subTest(
                'computer should pick first available cell when no moves have been played'):
            board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            expected_output = 1

            result = self.player.make_move(board)

            self.assertEqual(result, expected_output)

        with self.subTest(
                'computer should pick first available cell when moves have been played'):
            board = [['x', 2, 3], [4, 5, 6], [7, 8, 9]]
            expected_output = 2

            result = self.player.make_move(board)

            self.assertEqual(result, expected_output)
