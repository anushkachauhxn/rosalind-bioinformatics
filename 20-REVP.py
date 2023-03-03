# 20) Locating Restriction Sites
import sys
import os


def sortInput(lines):
    dna_string = ""
    for i in range(1, len(lines)):
        dna_string += lines[i].strip()
    return dna_string


def getReverseCompliment(str):
    compliment = ""
    for ch in reversed(str):
        if (ch == "A"):
            compliment += "T"
        elif (ch == "T"):
            compliment += "A"
        elif (ch == "C"):
            compliment += "G"
        elif (ch == "G"):
            compliment += "C"
    return compliment


def isReversePalindrome(str):
    compliment = getReverseCompliment(str)
    if (compliment == str):
        return True
    return False


class site_obj:
    def __init__(self, pos, str):
        self.pos = pos
        self.str = str
        self.len = len(str)


def locateRestrictionSites(str):
    locations = []
    for i in range(0, len(str)):
        for l in range(4, 13):
            if (i+l <= len(str)):
                substr = str[i: i+l]
                if (isReversePalindrome(substr)):
                    locations.append(site_obj(i+1, substr))
    return locations


def main():
    # Get multiline input
    lines = sys.stdin.readlines()
    dna_string = sortInput(lines)
    locations = locateRestrictionSites(dna_string)
    [print(x.pos, x.len) for x in locations]


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
