import os
import sys
import unittest

import nose2
from nose2.tools import params

from game import Frame, Game


class FrameTests(unittest.TestCase):
    def setUp(self):
        # We probably need a frame object every time
        self.frame = Frame()

    @params(
        (-1, ),
        (11, ),
    )
    def test_frame_first_roll_range(self, pins):
        self.assertRaises(ValueError, self.frame.roll, pins)

    @params(
        (0, 11),
        (1, 10),
        (9, 2),
        (10, 1),
    )
    def test_frame_second_roll_range(self, pins_1, pins_2):
        self.frame.roll(pins_1)
        self.assertRaises(ValueError, self.frame.roll, pins_2)

    def test_frame_third_roll_fails(self):
        self.frame.roll(1)
        self.frame.roll(2)
        self.assertRaises(Exception, self.frame.roll, 3)

    @params(
        (0, 0, 0),
        (1, 0, 1),
        (0, 1, 1),
        (1, 1, 2),
        (1, 9, 10),
        (5, 5, 10),
        (9, 1, 10),
    )
    def test_frame_score(self, pins_1, pins_2, score):
        self.frame.roll(pins_1)
        self.frame.roll(pins_2)
        self.assertEqual(self.frame.score, score)

    def test_frame_finished(self):
        self.assertFalse(self.frame.finished)
        self.frame.roll(0)
        self.assertFalse(self.frame.finished)
        self.frame.roll(0)
        self.assertTrue(self.frame.finished)


class GameTests(unittest.TestCase):
    def setUp(self):
        # We probably need a game object every time
        self.game = Game()

    @params(
        (-1, ),
        (11, ),
    )
    def test_game_roll_range(self, pins):
        self.assertRaises(ValueError, self.game.roll, pins)

    def test_gutter_game(self):
        for i in xrange(20):
            self.game.roll(0)
        self.assertEqual(self.game.score, 0)

    def test_1_game(self):
        for i in xrange(20):
            self.game.roll(1)
        self.assertEqual(self.game.score, 20)

    def test_game_finishes(self):
        for i in xrange(20):
            self.game.roll(0)
        self.assertRaises(RuntimeError, self.game.roll, 0)

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
