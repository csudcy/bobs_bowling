import os
import sys
import unittest

import nose2

from game import Game


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
