import random

class Frame(object):
    def __init__(self):
        pass

    def roll(self, pins):
        raise NotImplementedError()

    @property
    def pins_remaining(self):
        raise NotImplementedError()

    @property
    def score(self):
        raise NotImplementedError()

    @property
    def finished(self):
        raise NotImplementedError()

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
