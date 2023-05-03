import unittest
from player import Player, ComputerPlayer, SuperComputerPlayer


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


class TestSuperComputerPlayer(unittest.TestCase):
    def setUp(self):
        self.player = SuperComputerPlayer("Super Bot", "x")

    def test_computer_player(self):
        with self.subTest('has name'):
            expected_output = "Super Bot"
            result = self.player.get_name()
            self.assertEqual(result, expected_output)

        with self.subTest('has mark'):
            expected_output = "x"
            result = self.player.get_mark()
            self.assertEqual(result, expected_output)

    def test_make_move(self):
        test_cases = [{'board': [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                       'expected_move': 1},
                      {'board': [["o", 2, "o"], [4, 5, 6], [7, 8, 9]],
                       'expected_move': 2},
                      {'board': [["o", "x", "o"], ["x", "o", "x"], ["x", "o", 9]],
                       'expected_move': 9},
                      {'board': [["o", "x", "o"], ["x", "o", "x"], [8, "o", 9]],
                       'expected_move': 8},
                      ]

        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                expected_move = test_case['expected_move']
                result = self.player.make_move(test_case['board'])
                self.assertEqual(expected_move, result)

    def test_is_moves_left(self):
        test_cases = [
            {
                'name': "should return false when no moves left",
                'board': [['x', 'o', 'x'], ['x', 'o', 'x'], ['o', 'x', 'o']],
                'expected_result': False
            },
            {
                'name': "should return true when one move left",
                'board': [['x', 'o', 'x'], ['x', 'o', 'x'], ['o', 8, 'o']],
                'expected_result': True
            },
            {
                'name': "should return true when multiple moves left",
                'board': [['x', 'o', 'x'], ['x', 5, 'x'], ['o', 8, 'o']],
                'expected_result': True
            }
        ]

        for test_case in test_cases:
            with self.subTest(test_case=['name']):
                board = test_case['board']
                expected_result = test_case['expected_result']
                self.assertEqual(self.player.is_moves_left(board), expected_result)

    def test_evaluate(self):
        test_cases = [{'board': [['x', 'o', 'o'], ['o', 'x', 'x'], ['x', 8, 9]],
                       'expected_result': 10},
                      {'board': [['o', 'x', 'x'], ['x', 'o', 'o'], [7, 'x', 9]],
                       'expected_result': -10},
                      {'board': [['o', 'x', 'o'], ['x', 'x', 'o'], ['o', 'o', 'x']], 
                       'expected_result': 0}]

        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                expected_result = test_case['expected_result']
                result = self.player.evaluate(test_case['board'])
                self.assertEqual(result, expected_result)

    def test_minimax_cases(self):
        test_cases = [
            {'board': [['x', 'o', 2], [3, 'o', 5], [6, 'x', 'o']],
             'depth': 0,
             'is_max': True,
             'alpha': -float('inf'),
             'beta': float('inf'),
             'expected_result': 10},
            {'board': [['x', 'o', 'o'], ['o', 'x', 'x'], ['o', 'x', 'o']],
             'depth': 0,
             'is_max': False,
             'alpha': -float('inf'),
             'beta': float('inf'),
             'expected_result': -10},
            {'board': [[0, 'o', 'x'], ['o', 5, 6], ['x', 'o', 'x']],
             'depth': 0,
             'is_max': True,
             'alpha': -float('inf'),
             'beta': float('inf'),
             'expected_result': 0},
        ]

        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                result = self.player.minimax(test_case['board'],
                                            test_case['depth'],
                                            test_case['is_max'])
                expected_result = test_case['expected_result']
                self.assertEqual(result, expected_result)
