import random


class Frame(object):
    def __init__(self):
        self._pins_remaining = 10
        self._rolls_remaining = 2
        self._rolls = []

    def roll(self, pins):
        if self.finished:
            raise Exception('You have no rolls remaining in this frame!')
        if pins < 0:
            raise ValueError('You must roll a positive number of pins!')
        if pins > self._pins_remaining:
            raise ValueError(
                'You cannot roll {pins} pin(s) as there are only {pins_remaining} pin(s) left!'.format(
                    pins=pins,
                    pins_remaining=self._pins_remaining,
                )
            )
        self._rolls.append(pins)
        self._pins_remaining -= pins
        self._rolls_remaining -= 1

    @property
    def pins_remaining(self):
        # TODO: UNTESTED
        return self._pins_remaining

    def score(self, next_frame=None, max_rolls=None):
        # TODO: UNTESTED max_rolls
        if max_rolls:
            score = sum(self._rolls[:max_rolls])
        else:
            score = sum(self._rolls)

        if score == 10 and next_frame is not None:
            # There was a spare or a strike, get the next frame's score
            score += self._get_next_frame_score(next_frame)
        return score

    def _get_next_frame_score(self, next_frame):
        # TODO: UNTESTED
        max_rolls = 1
        if len(self._rolls) == 1:
            # This was a strike
            max_rolls = 2
        return next_frame.score(max_rolls=max_rolls)

    @property
    def finished(self):
        return (self._pins_remaining == 0) or (self._rolls_remaining == 0)


class Game(object):
    def __init__(self):
        # TODO: UNTESTED
        self._frames = [Frame() for i in xrange(10)]
        self._current_frame = 0

    # Requirements from Bob
    def roll(self, pins):
        # TODO: UNTESTED
        current_frame = self._frames[self._current_frame]
        current_frame.roll(pins)
        if current_frame.finished:
            self._current_frame += 1

    @property
    def score(self):
        # TODO: UNTESTED
        score = 0
        for i, frame in enumerate(self._frames):
            next_frame = None
            if i + 1 < len(self._frames):
                next_frame = self._frames[i + 1]
            score += frame.score(next_frame=next_frame)
        return score

    # Things that would be really useful
    @property
    def pins_remaining(self):
        # TODO: UNTESTED
        if self.finished:
            return 'Game over!'
        current_frame = self._frames[self._current_frame]
        return current_frame.pins_remaining

    @property
    def frame(self):
        # TODO: UNTESTED
        return self._current_frame

    @property
    def finished(self):
        # TODO: UNTESTED
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
        roll = random.randint(0, game.pins_remaining)
        print 'Rolling {roll}'.format(roll=roll)
        game.roll(roll)
