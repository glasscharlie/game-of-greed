import random
from collections import Counter


class Greed():

    def __init__(self, print_func=print, input_func=input):
        self._print = print_func
        self._input = input_func

    def calculate_score(self, current_dice_roll=(2, 2, 4, 4, 6, 6)):
        dice = []
        total = sum([])

        print('')

        r1 = random.randint(1, 6)
        r2 = random.randint(1, 6)
        r3 = random.randint(1, 6)
        r4 = random.randint(1, 6)
        r5 = random.randint(1, 6)
        r6 = random.randint(1, 6)

        dice.append(r1)
        dice.append(r2)
        dice.append(r3)
        dice.append(r4)
        dice.append(r5)
        dice.append(r6)

        print(dice)
        print('')

        cnt = Counter()

        for num in dice:
            cnt[num] += 1
        cnt

        print(cnt)
        print('')

        one = 100
        five = 50

        for key, value in cnt.items():

            if value == 1 and value == 2 and value == 3 and value == 4 and value == 5 and value == 6:
                total += (1500)
                break

        for key, value in cnt.items():
            if len(cnt) == 3 and value == 2:
                print(1500)

            if key == 1:
                if value == 6:
                    total += (one*40)
                elif value == 5:
                    total += (one*30)
                elif value == 4:
                    total += (one*20)
                elif value == 3:
                    total += (one*10)
                else:
                    total += (value*one)

            if key == 2:
                if value == 6:
                    total += (800)
                elif value == 5:
                    total += (600)
                elif value == 4:
                    total += (400)
                elif value == 3:
                    total += (200)
                else:
                    total += (0)

            if key == 3:
                if value == 6:
                    total += (1200)
                elif value == 5:
                    total += (900)
                elif value == 4:
                    total += (600)
                elif value == 3:
                    total += (300)
                else:
                    total += (0)

            if key == 4:
                if value == 6:
                    total += (1600)
                elif value == 5:
                    total += (1200)
                elif value == 4:
                    total += (800)
                elif value == 3:
                    total += (400)
                else:
                    total += (0)

            if key == 5:
                if value == 6:
                    total += (five*40)
                elif value == 5:
                    total += (five*30)
                elif value == 4:
                    total += (five*20)
                elif value == 3:
                    total += (five*10)
                else:
                    total += (value*five)

            if key == 6:
                if value == 6:
                    total += (2400)
                elif value == 5:
                    total += (1800)
                elif value == 4:
                    total += (1200)
                elif value == 3:
                    total += (600)
                else:
                    total += (0)

        print(total)

    def play(self, user_response=None):
        self._print('Welcome to Game of Greed!')
        response = self._input('Wanna play? ')

        if response == 'y' or user_response == 'y':
            self._print('Great! Check back tomorrow!')
        else:
            self._print('OK. Maybe another time')


if __name__ == "__main__":
    game = Greed()
    game.play()