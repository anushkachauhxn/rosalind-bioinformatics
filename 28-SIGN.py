# 28) Enumerating Oriented Gene Orderings
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
    print(n*n*count)


def listPermutations(n):
    words = [None] * n

    # To make it dynamic, find a way to create and use p1, p2 etc dynamically
    for p1, p2, p3, p4 in product(range(1, n+1), repeat=n):
        words[0] = p1
        words[1] = p2
        words[2] = p3
        words[3] = p4

        if (checkForDuplicates(words)):
            continue

        for a1, a2, a3, a4 in product(range(2), repeat=n):
            if (a1 == 1):
                words[0] = p1
            elif (a1 == 0):
                words[0] = -p1

            if (a2 == 1):
                words[1] = p2
            elif (a2 == 0):
                words[1] = -p2

            if (a3 == 1):
                words[2] = p3
            elif (a3 == 0):
                words[2] = -p3

            if (a4 == 1):
                words[3] = p4
            elif (a4 == 0):
                words[3] = -p4

            print(*words)


def main():
    n = int(input())
    countPermutations(n)
    listPermutations(n)


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
