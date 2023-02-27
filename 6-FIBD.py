# 4) Mortal Fibonacci Rabbits
import sys
import os


def recurrenceMortalRabits(n, m):
    rabbits = [1, 1, 1]  # indexes: -1, 0, 1

    for _ in range(2, n):
        if (m+1 > len(rabbits)):
            f = rabbits[-1] + rabbits[-2] - 0
        else:
            # Logic: F(n) = F(n-1) + F(n-2) + F(n-m)
            f = rabbits[-1] + rabbits[-2] - rabbits[-(m+1)]
        rabbits.append(f)

    return (rabbits[-1])


def main():
    n, m = map(int, input().split())
    print(recurrenceMortalRabits(n, m))


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
