# 4) Rabbits and Recurrence Relations
import sys
import os


def recurrenceRabits(n, k):
    f1 = 1
    f2 = 1
    for _ in range(3, n+1):
        f3 = f2 + f1*k
        f1 = f2
        f2 = f3
    return (f2)


def main():
    n, k = map(int, input().split())
    print(recurrenceRabits(n, k))


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
