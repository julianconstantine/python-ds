__author__ = 'Julian'

import random
target = "dave"
letters = "abcdefghijklmnopqrstuvwxyz"
guess = "jack"
count = 0

while guess != target:
    guess = ""
    count += 1

    for n in range(len(target)):
        guess += letters[random.randrange(0, 26)]


print(count)
print(guess)

