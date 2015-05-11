import random


class Frame(object):
    def __init__(self):
        self._pins_remaining = 10
        self._rolls_total = 2
        self._rolls_remaining = self._rolls_total
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

    def format_game(game):
        def format_frame(frame, running_score):
            """
            *******
            * 1 / *
            * 300 *
            *******
            """
            w = frame._rolls_total * 2 + 3

            # Generate the rolls portion
            rolls = []
            score = 0
            for roll in frame._rolls:
                if roll == 10:
                    rolls.append('X')
                else:
                    score += roll
                    if score == 10:
                        rolls.append('/')
                    else:
                        rolls.append(str(roll))
            while len(rolls) < frame._rolls_total:
                rolls.append(' ')

            # Generate the total portion
            if frame.finished:
                total_score = str(running_score)
            else:
                total_score = ''
            while len(total_score) < w-4:
                total_score = ' ' + total_score

            # Return everything
            return [
                '*'*w,
                '* %s *' % ' '.join(rolls),
                '*%s*' % ('-'*(w-2)),
                '* %s *' % total_score,
                '*'*w,
            ]

        output = ['', '', '', '', '']
        running_score = 0
        for i in xrange(len(game._frames)):
            frame = game._frames[i]
            if i+1 < len(game._frames):
                next_frame = game._frames[i+1]
            else:
                next_frame = None
            running_score += frame.score(next_frame)
            frame_output = format_frame(frame, running_score)
            for i in xrange(len(frame_output)):
                output[i] += frame_output[i]
        return '\n'.join(output)

    game = Game()
    while (True):
        print format_game(game)
        print
        if game.finished:
            break
        game.roll(random.randint(0, game.pins_remaining))
