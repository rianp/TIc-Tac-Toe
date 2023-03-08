import unittest
from main import *


class TestConsole(unittest.TestCase):
    def test_console_greeting_returns_true(self):
        console_test = Console()
        self.assertTrue(console_test.greeting())
