from game_of_greed import Game

# Welcome Testing


def test_welcome():
    prints = [
        "Welcome to Game of Greed!",
        "Wanna play? ",
        "OK. Maybe another time",
        "Great! Check back tomorrow!",
    ]

    def print_for_testing(message):
        assert message == prints.pop(0)

    game = Game(print_for_testing, print_for_testing)
    game.play()


def test_welcome_is_shown():
    prints = [
        "Welcome to Game of Greed!",
        "Wanna play? ",
        "OK. Maybe another time",
        "Great! Check back tomorrow!",
    ]

    def print_for_testing(message):
        assert message == prints.pop(0)

    game = Game(print_for_testing, print_for_testing)
    game.play()


def test_response_yes():
    prints = [
        "Welcome to Game of Greed!",
        "Wanna play? ",
        "Great! Check back tomorrow!",
        "OK. Maybe another time",
    ]

    def print_for_testing(message):
        assert message == prints.pop(0)

    game = Game(print_for_testing, print_for_testing)
    game.play("y")


# Testing Zilch


def test_none():
    actual = Game.score_game(Game(), (6, 2, 3, 2, 6, 4))
    assert actual == 0


# Testing 1s


def test_one_one():
    game = Game()
    assert game.score_game((1, 2, 2, 3, 4, 4)) == 100


def test_two_ones():
    game = Game()
    assert game.score_game((1, 1, 2, 3, 3, 4)) == 200


def test_three_ones():
    game = Game()
    assert game.score_game((1, 1, 1, 2, 3, 4)) == 1000


def test_four_ones():
    game = Game()
    assert game.score_game((1, 1, 1, 1, 3, 4)) == 2000


def test_five_ones():
    game = Game()
    assert game.score_game((1, 1, 1, 1, 1, 4)) == 3000


def test_all_ones():
    game = Game()
    assert game.score_game((1, 1, 1, 1, 1, 1)) == 4_000


# Testing 2s


def test_one_two():
    game = Game()
    assert game.score_game((2, 3, 3, 4, 6, 4)) == 0


def test_two_twos():
    game = Game()
    assert game.score_game((2, 2, 3, 4, 6, 4)) == 0


def test_three_twos():
    game = Game()
    assert game.score_game((2, 2, 2, 4, 6, 4)) == 200


def test_four_twos():
    game = Game()
    assert game.score_game((2, 2, 2, 2, 6, 4)) == 400


def test_five_twos():
    game = Game()
    assert game.score_game((2, 2, 2, 2, 2, 4)) == 600


def test_all_twos():
    game = Game()
    assert game.score_game((2, 2, 2, 2, 2, 2)) == 800


# Testing 3s


def test_one_three():
    game = Game()
    assert game.score_game((2, 2, 3, 4, 6, 4)) == 0


def test_two_threes():
    game = Game()
    assert game.score_game((2, 3, 3, 4, 6, 4)) == 0


def test_three_threes():
    game = Game()
    assert game.score_game((3, 3, 3, 2, 6, 4)) == 300


def test_four_threes():
    game = Game()
    assert game.score_game((3, 3, 3, 3, 6, 4)) == 600


def test_five_threes():
    game = Game()
    assert game.score_game((3, 3, 3, 3, 3, 4)) == 900


def test_many_threes():
    game = Game()
    assert game.score_game((3, 3, 3, 3, 3, 3)) == 1_200


# Test 4s


def test_one_four():
    game = Game()
    assert game.score_game((2, 2, 3, 3, 6, 4)) == 0


def test_two_fours():
    game = Game()
    assert game.score_game((2, 2, 3, 6, 4, 4)) == 0


def test_three_fours():
    game = Game()
    assert game.score_game((2, 2, 3, 4, 4, 4)) == 400


def test_four_fours():
    game = Game()
    assert game.score_game((2, 2, 4, 4, 4, 4)) == 800


def test_five_fours():
    game = Game()
    assert game.score_game((2, 4, 4, 4, 4, 4)) == 1_200


def test_many_fours():
    game = Game()
    assert game.score_game((4, 4, 4, 4, 4, 4)) == 1_600


# Test 5s
def test_one_five():
    game = Game()
    assert game.score_game((2, 2, 3, 5, 6, 4)) == 50


def test_two_fives():
    game = Game()
    assert game.score_game((5, 2, 5, 2, 6, 4)) == 100


def test_three_fives():
    game = Game()
    assert game.score_game((5, 5, 5, 2, 6, 4)) == 500


def test_four_fives():
    game = Game()
    assert game.score_game((5, 5, 5, 5, 6, 4)) == 1_000


def test_five_fives():
    game = Game()
    assert game.score_game((5, 5, 5, 5, 5, 4)) == 1_500


def test_many_fives():
    game = Game()
    assert game.score_game((5, 5, 5, 5, 5, 5)) == 2_000


# Test 6's


def test_one_six():
    game = Game()
    assert game.score_game((2, 2, 3, 3, 6, 4)) == 0


def test_two_sixes():
    game = Game()
    assert game.score_game((2, 2, 3, 3, 6, 6)) == 0


def test_three_sixes():
    game = Game()
    assert game.score_game((6, 2, 3, 6, 6, 4)) == 600


def test_four_sixes():
    game = Game()
    assert game.score_game((2, 2, 6, 6, 6, 6)) == 1_200


def test_five_sixes():
    game = Game()
    assert game.score_game((2, 6, 6, 6, 6, 6)) == 1_800


def test_many_sixes():
    game = Game()
    assert game.score_game((6, 6, 6, 6, 6, 6)) == 2_400


# # Straight

# def test_straight():
#     game = Greed()
#     assert game.score_game((1,2,3,4,5,6)) == 1_500
# def test_reverse_straight():
#     game = Greed()
#     assert game.score_game((6,5,4,3,2,1)) == 1_500


# # Three Pairs

# def test_three_pairs():
#     game = Greed()
#     assert game.score_game((2,2,4,4,6,6)) == 1_500

# Double Trio


def test_two_trios():
    game = Game()
    assert game.score_game((2, 2, 2, 3, 3, 3)) == 500


def test_two_mixed_up_trios():
    game = Game()
    assert game.score_game((4, 6, 4, 6, 4, 6)) == 1000


# Added 1s


def test_added_ones():
    game = Game()
    assert game.score_game((3, 3, 3, 4, 6, 1)) == 400


def test_two_added_ones():
    game = Game()
    assert game.score_game((6, 6, 4, 1, 1, 6)) == 800


# Added 5s


def test_one_leftover_fives():
    game = Game()
    assert game.score_game((3, 3, 3, 4, 6, 5)) == 350


def test_two_leftover_fives():
    game = Game()
    assert game.score_game((6, 5, 4, 6, 5, 6)) == 700