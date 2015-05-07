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
        ([0, 0], ),
        ([0, 10], ),
        ([1, 1], ),
        ([1, 9], ),
        ([5, 5], ),
        ([9, 1], ),
        ([10], ),
    )
    def test_finished(self, rolls):
        self.assertFalse(self.frame.finished)
        for roll in rolls[:-1]:
            self.frame.roll(roll)
            self.assertFalse(self.frame.finished)
        self.frame.roll(rolls[-1])
        self.assertTrue(self.frame.finished)

    @params(
        (-1, ),
        (11, ),
    )
    def test_roll_limits(self, roll):
        self.assertRaises(ValueError, self.frame.roll, roll)

    @params(
        (0, -1, ),
        (0, 11, ),
        (5, -1, ),
        (5, 11, ),
    )
    def test_second_roll_limits(self, roll1, roll2):
        self.frame.roll(roll1)
        self.assertRaises(ValueError, self.frame.roll, roll2)

    @params(
        ([0, 0, 0], ),
        ([0, 10, 0], ),
        ([5, 5, 0], ),
        ([10, 0], ),
    )
    def test_too_many_rolls(self, rolls):
        for roll in rolls[:-1]:
            self.frame.roll(roll)
        # Last roll should error
        self.assertRaises(Exception, self.frame.roll, rolls[-1])

    @params(
        ([0], 0),
        ([1], 1),
        ([5], 5),
        ([9], 9),
        ([0, 0], 0),
        ([0, 10], 10),
        ([1, 1], 2),
        ([1, 9], 10),
        ([5, 5], 10),
        ([9, 1], 10),
        ([10], 10),
    )
    def test_score(self, rolls, final_score):
        for roll in rolls:
            self.frame.roll(roll)
        self.assertEqual(self.frame.score(), final_score)

    @params(
        # Check not getting spare/strike doesnt change scores
        ([0, 0], [0], 0),
        ([0, 0], [1], 1),
        ([0, 0], [5], 5),
        ([0, 0], [9], 9),
        ([0, 1], [0], 1),
        ([0, 1], [1], 2),
        ([0, 1], [5], 6),
        ([0, 1], [9], 10),

        # Check getting a spare only takes the first roll
        ([5, 5], [0, 1], 11),
        ([5, 5], [1, 1], 13),
        ([5, 5], [5, 1], 21),
        ([5, 5], [9, 1], 29),
        ([5, 5], [10], 30),

        # Check getting a strike uses both rolls
        ([10], [0, 1], 12),
        ([10], [1, 1], 14),
        ([10], [5, 1], 22),
        ([10], [9, 1], 30),
        ([10], [10], 30),
    )
    def test_score_with_next_frame(
            self,
            frame_1_rolls,
            frame_2_rolls,
            final_score
        ):
        f1 = Frame()
        for roll in frame_1_rolls:
            f1.roll(roll)
        f2 = Frame()
        for roll in frame_2_rolls:
            f2.roll(roll)
        f1_score = f1.score(f2)
        f2_score = f2.score()
        total_score = f1_score + f2_score
        self.assertEqual(total_score, final_score)


class GameTests(unittest.TestCase):
    def setUp(self):
        # We probably need a game object every time
        self.game = Game()


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
