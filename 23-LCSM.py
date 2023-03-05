# 23) Finding a Shared Motif
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


def longestCommonSubstring(dna_strings):
    ref = min(dna_strings, key=len)  # taking shortest string as reference
    n = len(dna_strings)
    l = len(ref)
    lcs = ""

    for i in range(l):
        for j in range(i+1, l+1):
            substr = ref[i:j]

            k = 1
            for k in range(n):
                if (substr not in dna_strings[k]):
                    break

            if (k == n-1 and len(substr) > len(lcs)):
                lcs = substr
    return lcs


def main():
    # Get multiline input
    lines = sys.stdin.readlines()
    dna_strings = sortInput(lines)
    print(longestCommonSubstring(dna_strings))


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
