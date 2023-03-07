# 26) Finding a Spliced Motif
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


def findSubsequenceIndices(s, t):
    indices = []
    progress = -1

    while (len(indices) < len(t) and progress < len(s)-1):
        next = t[len(indices)]  # next symbol to search
        for i in range(progress+1, len(s)):
            if (s[i] == next):
                indices.append(i+1)
                break
        progress = i

    return indices


def main():
    lines = sys.stdin.readlines()
    dna_strings = sortInput(lines)
    print(*findSubsequenceIndices(dna_strings[0], dna_strings[1]))


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
