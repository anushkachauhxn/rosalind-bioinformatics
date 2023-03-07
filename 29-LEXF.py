# 29) Enumerating k-mers Lexicographically
import os
import sys
from itertools import combinations_with_replacement


def getAllLexograhicalStrings(n, A):
    combinations = list(combinations_with_replacement(A, n)) + \
        list(combinations_with_replacement(reversed(A), n))

    strings = []
    for x in combinations:
        str = "".join(x)
        if (str not in strings):
            strings.append(str)
    strings.sort()

    return strings


def main():
    A = list(input().split(" "))
    n = int(input())
    print(*getAllLexograhicalStrings(n, A), sep='\n')


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
