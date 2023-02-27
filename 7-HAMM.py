# 7) Counting Point Mutations
import sys
import os


def findHammingDistance(s, t):
    count = 0
    for i in range(0, len(s)):
        if (s[i] != t[i]):
            count += 1
    return count


def main():
    s = input()
    t = input()
    print(findHammingDistance(s, t))


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
