# 12) Calculating Expected Offspring
import sys
import os


def calculateExpectedOffspring(numOfCouples):
    dominant_prob = [1, 1, 1, 0.75, 0.5, 0]
    exp_count = 0

    for i in range(0, len(numOfCouples)):
        exp_count += dominant_prob[i] * numOfCouples[i]

    return (exp_count * 2)


def main():
    numOfCouples = list(map(int, input().split()))
    print(calculateExpectedOffspring(numOfCouples))


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
