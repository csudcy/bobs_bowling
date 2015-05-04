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
    def pins_remaining(self):
        # UNTESTED
        return self._pins_remaining

    @property
    def score(self):
        return self._score

    @property
    def finished(self):
        return self._balls_remaining <= 0

class Game(object):
    def __init__(self):
        self._frames = [
            Frame()
            for i in xrange(10)
        ]
        self._current_frame = 0

    # Requirements from Bob
    def roll(self, pins):
        if self.finished:
            raise RuntimeError('The game is over!')
        frame = self._frames[self._current_frame]
        frame.roll(pins)
        if frame.finished:
            self._current_frame += 1

    @property
    def score(self):
        return sum([
            frame.score
            for frame in self._frames
        ])

    # Things that would be really useful
    @property
    def pins_remaining(self):
        # UNTESTED
        if self.finished:
            return 'Game over!'
        frame = self._frames[self._current_frame]
        return frame.pins_remaining

    @property
    def frame(self):
        # UNTESTED
        return self._current_frame

    @property
    def finished(self):
        return self._current_frame >= len(self._frames)

if __name__ == '__main__':
    game = Game()
    while (True):
        print '{score} @ frame {frame} ({pins_remaining} pins remaining)'.format(
            frame=game.frame,
            score=game.score,
            pins_remaining=game.pins_remaining,
        )
        if game.finished:
            break
        game.roll(random.randint(0, game.pins_remaining))
