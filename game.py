import random

class Game(object):
    def __init__(self):
        self._score = 0

    # Requirements from Bob
    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise Exception('Pins must be between 1 and 10')
        self._score += pins

    @property
    def score(self):
        return self._score

    # Things that would be really useful
    @property
    def pins_remaining(self):
        raise NotImplementedError()

    @property
    def frame(self):
        raise NotImplementedError()

    @property
    def finished(self):
        raise NotImplementedError()

if __name__ == '__main__':
    game = Game()
    while (not game.finished):
        game.roll(random.randint(game.pins_remaining))
        print '{score} @ frame {frame} ({pins_remaining} pins remaining)'.format(
            frame=game.frame,
            score=game.score,
            pins_remaining=game.pins_remaining,
        )
