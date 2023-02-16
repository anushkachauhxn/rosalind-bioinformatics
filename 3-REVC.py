# 3) Complementing a Strand of DNA
import sys
import os


def complimentDNA(dna):
    # Produce reverse compliment of given string
    compliment = ""
    for ch in reversed(dna):
        if (ch == "A"):
            compliment += "T"
        elif (ch == "T"):
            compliment += "A"
        elif (ch == "C"):
            compliment += "G"
        elif (ch == "G"):
            compliment += "C"
    return compliment


def main():
    text = input()
    print(complimentDNA(text))


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
