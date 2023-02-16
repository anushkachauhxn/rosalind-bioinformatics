# 5) Computing GC Content
import sys
import os


class dna_obj:
    def __init__(self, id, str):
        self.id = id
        self.str = str
        self.gc = (self.str.count('G') + self.str.count('C')) * 100 / len(str)


def getMaxGC(lines):
    # Sort input into suitable data objects
    data = []
    for index in range(0, len(lines), 2):
        dna = dna_obj(lines[index], lines[index+1])
        data.append(dna)

    # Getting max - https://stackoverflow.com/a/46796164/12302691
    max_dna = max(data, key=lambda node: node.gc)
    return (max_dna.id[1:] + str(max_dna.gc))


def main():
    # Get multiline input
    lines = sys.stdin.readlines()
    print(getMaxGC(lines))


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
