# 25) Introduction to Random Strings
import os
import sys
from math import log10


def findGC(str):
    return (str.count('G') + str.count('C')) / len(str)


def getGCProbability(s, gc):
    prob = 0
    for ch in s:
        if (ch == 'G' or ch == 'C'):
            prob += log10(gc / 2)
        elif (ch == 'A' or ch == 'T'):
            prob += log10((1-gc) / 2)
    return prob


def main():
    s = input()
    A = list(map(float, input().split()))
    B = []
    for i in range(len(A)):
        B.append(getGCProbability(s, A[i]))
    print(*B)


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
