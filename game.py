import random

class Game(object):
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
    while (not game.finished):
        game.roll(random.randint(game.pins_remaining))
        print '{score} @ frame {frame} ({pins_remaining} pins remaining)'.format(
            frame=game.frame,
            score=game.score,
            pins_remaining=game.pins_remaining,
        )
