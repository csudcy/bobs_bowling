import random

class Frame(object):
    def __init__(self):
        #self._number = number
        self._balls_remaining = 2
        self._pins_remaining = 10
        self._score = 0

    def roll(self, pins):
        if self.finished:
            raise Exception('There are no more balls in this frame!')
        if pins < 0:
            raise ValueError('Pins cannot be negative!')
        if pins > self._pins_remaining:
            raise ValueError('Cannot roll more than the pins remaining in this frame!')
        self._balls_remaining -= 1
        self._pins_remaining -= pins
        self._score += pins

    @property
    def score(self):
        return self._score

    @property
    def finished(self):
        return self._balls_remaining <= 0

class Game(object):
    def __init__(self):
        self._score = 0

    # Requirements from Bob
    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError('Pins must be between 1 and 10')
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
