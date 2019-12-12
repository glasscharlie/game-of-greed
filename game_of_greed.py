import random
from collections import Counter


class Game:
    def __init__(self, print_func=print, input_func=input):
        self._print = print_func
        self._input = input_func

    def roll_dice(self):

        """
        Simulates rolling 6 dice and appends those values into the below dice object.
        """

        dice = []
        dice.append(random.randint(1, 6))
        dice.append(random.randint(1, 6))
        dice.append(random.randint(1, 6))
        dice.append(random.randint(1, 6))
        dice.append(random.randint(1, 6))
        dice.append(random.randint(1, 6))

        return dice

    # Calculate the score

    def score_game(self, dice):
        """
        Every possibiblity of scoring has its own instance. Starting with the most rare case to the most common case to avoid any miscalculations.
        """
        total = 0
        cnt = Counter(dice)

        """
        What the counter is doing is adding the dice to a dictionary where it is then adding up the values of each value. So say you roll 4 2s, the dictionary under the key of 2 will be 4 as a value.
        """

        one = 100
        five = 50

        for key, value in cnt.items():

            # Straight Score
            if (
                value == 1
                and value == 2
                and value == 3
                and value == 4
                and value == 5
                and value == 6
            ):
                total += 1500
                break

            # One Score
            if key == 1:
                if value == 6:
                    total += one * 40
                elif value == 5:
                    total += one * 30
                elif value == 4:
                    total += one * 20
                elif value == 3:
                    total += one * 10
                else:
                    total += value * one

            # Two Score
            if key == 2:
                if value == 6:
                    total += 800
                elif value == 5:
                    total += 600
                elif value == 4:
                    total += 400
                elif value == 3:
                    total += 200
                else:
                    total += 0

            # Three Score
            if key == 3:
                if value == 6:
                    total += 1200
                elif value == 5:
                    total += 900
                elif value == 4:
                    total += 600
                elif value == 3:
                    total += 300
                else:
                    total += 0

            # Four Score
            if key == 4:
                if value == 6:
                    total += 1600
                elif value == 5:
                    total += 1200
                elif value == 4:
                    total += 800
                elif value == 3:
                    total += 400
                else:
                    total += 0

            # Five Score
            if key == 5:
                if value == 6:
                    total += five * 40
                elif value == 5:
                    total += five * 30
                elif value == 4:
                    total += five * 20
                elif value == 3:
                    total += five * 10
                else:
                    total += value * five

            # Six Score
            if key == 6:
                if value == 6:
                    total += 2400
                elif value == 5:
                    total += 1800
                elif value == 4:
                    total += 1200
                elif value == 3:
                    total += 600
                else:
                    total += 0

        return total

        print(total)

    def play(self, user_response=None):

        """
        Prints  Prints a beginning prompt to the user and greeting.
        """

        self._print("Welcome to Game of Greed!")
        response = self._input("Wanna play? ")

        if response == "y" or user_response == "y":
            self._print("Great! Check back tomorrow!")
        else:
            self._print("OK. Maybe another time")


if __name__ == "__main__":
    game = Game()
    game.play()