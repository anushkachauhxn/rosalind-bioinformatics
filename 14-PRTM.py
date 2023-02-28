# 14) Calculating Protein Mass
import sys
import os

MONOISOTOPIC_MASS_TABLE = {
    'A':   71.03711,
    'C':   103.00919,
    'D':   115.02694,
    'E':   129.04259,
    'F':   147.06841,
    'G':   57.02146,
    'H':   137.05891,
    'I':   113.08406,
    'K':   128.09496,
    'L':   113.08406,
    'M':   131.04049,
    'N':   114.04293,
    'P':   97.05276,
    'Q':   128.05858,
    'R':   156.10111,
    'S':   87.03203,
    'T':   101.04768,
    'V':   99.06841,
    'W':   186.07931,
    'Y':   163.06333,
}


def getAminoWeight(protein):
    weight = 0
    for i in range(0, len(protein)):
        weight += MONOISOTOPIC_MASS_TABLE[protein[i]]
    return weight


def main():
    protein = input()
    print(getAminoWeight(protein))


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
