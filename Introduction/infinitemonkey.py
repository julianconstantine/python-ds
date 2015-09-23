__author__ = 'Julian'

import random

def randString(lenstr):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    randstr = ""

    for n in range(lenstr):
        index = random.randrange(27)
        randstr += alphabet[index]

    return randstr


def strScore(test, target):
    score = 0

    for j in range(len(target)):
        if test[j] == target[j]:
            score += 1

    score /= len(target)

    return score


def main():
    target = "methinks it is like a weasel"
    count = 0
    oldscore = 0

    while strScore(randString(len(target)), target) < 1:
        count += 1


    print(count)

