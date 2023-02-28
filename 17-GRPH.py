# 17) Overlap Graphs
import sys
import os

data = []


class dna_obj:
    def __init__(self, id, str):
        self.id = id[1:]
        self.str = str
        self.prefix = str[:3]
        self.suffix = str[-3:]


def sortInput(lines):
    def isIdString(str):
        if (str.startswith(">")):
            return True
        return False

    for i in range(0, len(lines)):
        if (isIdString(lines[i])):
            id = lines[i].strip()
            str = ""
            for j in range(i+1, len(lines)):
                if (isIdString(lines[j])):
                    break
                str += lines[j].strip()

            dna = dna_obj(id, str)
            data.append(dna)


def createAdjacencyList():
    adj_list = []
    for s in data:
        for t in data:
            if (s.str != t.str):
                if (s.suffix == t.prefix):
                    adj_list.append([s.id, t.id])
    return adj_list


def main():
    # Get multiline input
    lines = sys.stdin.readlines()
    sortInput(lines)
    A = createAdjacencyList()
    for x in A:
        print(*x)


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
