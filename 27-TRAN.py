# 27) Transitions and Transversions
import sys
import os


def sortInput(lines):
    def isIdString(str):
        if (str.startswith(">")):
            return True
        return False

    dna_strings = []
    for i in range(0, len(lines)):
        if (isIdString(lines[i])):
            str = ""
            for j in range(i+1, len(lines)):
                if (isIdString(lines[j])):
                    break
                str += lines[j].strip()
            dna_strings.append(str)
    return dna_strings


def getTranRatio(s1, s2):
    transitions = [['A', 'G'], ['C', 'T']]
    transversions = [['A', 'C'], ['G', 'C'], ['A', 'T'], ['G', 'T']]
    transitionCount = 0
    transversionCount = 0

    for i in range(len(s1)):
        mutation = [s1[i], s2[i]]
        if (mutation in transitions or mutation[::-1] in transitions):
            transitionCount += 1
        if (mutation in transversions or mutation[::-1] in transversions):
            transversionCount += 1

    return (transitionCount / transversionCount)


def main():
    lines = sys.stdin.readlines()
    dna_strings = sortInput(lines)
    print(getTranRatio(dna_strings[0], dna_strings[1]))


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
