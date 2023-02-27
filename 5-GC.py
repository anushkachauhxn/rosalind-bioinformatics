# 5) Computing GC Content
import sys
import os

data = []


class dna_obj:
    def __init__(self, id, str):
        self.id = id
        self.str = str
        self.gc = (self.str.count('G') + self.str.count('C')) * 100 / len(str)


def getMaxGC():
    # Getting max - https://stackoverflow.com/a/46796164/12302691
    max_dna = max(data, key=lambda node: node.gc)
    return (max_dna.id[1:] + str(max_dna.gc))


def sortInput(lines):
    def isIdString(str):
        if (str.startswith(">")):
            return True
        return False

    for i in range(0, len(lines)):
        if (isIdString(lines[i])):
            id = lines[i]
            str = ""
            for j in range(i+1, len(lines)):
                if (isIdString(lines[j])):
                    break
                str += lines[j].strip()

            dna = dna_obj(id, str)
            data.append(dna)


def main():
    # Get multiline input
    lines = sys.stdin.readlines()
    sortInput(lines)
    print(getMaxGC())


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
