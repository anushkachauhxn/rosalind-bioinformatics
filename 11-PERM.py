# 9) Enumerating Gene Orders
import sys
import os
from itertools import product


def checkForDuplicates(list):
    if len(list) == len(set(list)):
        return False
    else:
        return True


def countPermutations(n):
    count = 1
    for x in range(1, n+1):
        count = count * x
    print(count)


def listPermutations(n):
    words = [None] * n

    # To make it dynamic, find a way to create and use p1, p2 etc dynamically
    for p1, p2, p3, p4, p5, p6 in product(range(1, n+1), repeat=n):
        words[0] = p1
        words[1] = p2
        words[2] = p3
        words[3] = p4
        words[4] = p5
        words[5] = p6
        if (checkForDuplicates(words)):
            continue
        print(p1, p2, p3, p4, p5, p6)


def main():
    n = int(input())
    countPermutations(n)
    listPermutations(n)


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
