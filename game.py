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
        raise NotImplementedError()

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
        pass

    # Requirements from Bob
    def roll(self, pins):
        raise NotImplementedError()

    @property
    def score(self):
        raise NotImplementedError()

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
    while (True):
        print '{score} @ frame {frame} ({pins_remaining} pins remaining)'.format(
            frame=game.frame,
            score=game.score,
            pins_remaining=game.pins_remaining,
        )
        if game.finished:
            break
        game.roll(random.randint(0, game.pins_remaining))
