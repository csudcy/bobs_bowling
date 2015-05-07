# Bobs Bowling

My implementations of [Uncle Bobs bowling kata](http://butunclebob.com/ArticleS.UncleBob.TheBowlingGameKata)

Notes:
* You need `nose2` to run the tests
* Run `python game.py` to play a random game
* Run `python tests.py` to run the unit tests

Learnings:
* V1:
** Method names inside TestCase's have to be globally uniqe
** Game is too big for 30 minutes; concentrate on Frame first next time
* V2:
** Starting with Frame was much better
** I don't like max_rolls being pass in to score
** Might have written too many params (18) for `test_score_with_next_frame`
