# 15) Partial Permutations
import sys
import os


def numOfPartialPermutations(n, k):
    subarrays = 1
    for i in range(0, k):
        subarrays *= (n-i)
    return (subarrays % 1000000)


def main():
    n, k = map(int, input().split())
    print(numOfPartialPermutations(n, k))


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
