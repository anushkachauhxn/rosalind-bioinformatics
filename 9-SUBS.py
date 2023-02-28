# 9) Finding a Motif in DNA
import sys
import os


def findMotifs(s, t):
    positions = []
    index = -1
    while True:
        index = s.find(t, index+1)
        if (index == -1):
            break
        positions.append(index+1)
    return positions


def main():
    s = input()
    t = input()
    print(*findMotifs(s, t))


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
