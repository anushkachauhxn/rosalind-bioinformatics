# 1) Counting DNA Nucleotides
import sys
import os


def numOfNeuclotides(text):
    numOfA = text.count('A')
    numOfC = text.count('C')
    numOfG = text.count('G')
    numOfT = text.count('T')
    return str(numOfA) + " " + str(numOfC) + " " + str(numOfG) + " " + str(numOfT)


def main():
    text = input()
    print(numOfNeuclotides(text))


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
