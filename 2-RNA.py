# 2) Transcribing DNA into RNA
import sys
import os


def transcribeToRNA(dna):
    rna = dna.replace("T", "U")
    return rna


def main():
    text = input()
    print(transcribeToRNA(text))


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
