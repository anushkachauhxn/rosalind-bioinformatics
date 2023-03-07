# 29) Enumerating k-mers Lexicographically
import os
import sys
from itertools import product


def getAllLexograhicalStrings(n, A):
    strings = []
    for i, j in product(range(len(A)), repeat=n):
        str = A[i]+A[j]
        strings.append(str)
    return strings


def main():
    A = list(input().split(" "))
    n = int(input())
    [print(x) for x in getAllLexograhicalStrings(n, A)]


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
