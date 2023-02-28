# 8) Mendel's First Law
import sys
import os


def findDominantProb(k, m, n):
    dom = (k*m) + (k*n) + (m*n)/2 + k*(k-1)/2 + 3*m*(m-1)/8
    total = (k*m) + (k*n) + (m*n) + k*(k-1)/2 + m*(m-1)/2 + n*(n-1)/2
    return (dom / total)


def main():
    k, m, n = map(int, input().split())
    print(findDominantProb(k, m, n))


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
