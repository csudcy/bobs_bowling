import os
import sys
import unittest

import nose2
from nose2.tools import params

from game import Game


class GameTests(unittest.TestCase):
    def setUp(self):
        # We probably need a game object every time
        self.game = Game()

    @params(
        (-1, ),
        (11, ),
    )
    def test_roll_range(self, pins):
        self.assertRaises(Exception, self.game.roll, pins)

    def test_gutter_game(self):
        for i in xrange(20):
            self.game.roll(0)
        self.assertEqual(self.game.score, 0)

    def test_1_game(self):
        for i in xrange(20):
            self.game.roll(1)
        self.assertEqual(self.game.score, 20)

    # def test_a_strike(self):
    #     self.game.roll(10)
    #     self.game.roll(1)
    #     self.game.roll(1)
    #     # Score should be 10 + 2 * (1 + 1) = 14
    #     self.assertEqual(self.game.score, 14)


if __name__ == '__main__':
    # Construct command line
    CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
    PARENT_DIRECTORY = os.path.split(CURRENT_DIRECTORY)[0]
    argv = [
        sys.argv[0],
        '-s',
        PARENT_DIRECTORY
    ]

    # Run the tests with exit=False so we can print coverage after
    nose2.discover(argv=argv)
