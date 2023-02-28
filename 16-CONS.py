# 16) Consensus and Profile
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


def createProfileMatrix(dna_strings):
    # dna_strings can be seen as a matrix of n rows x m columns
    n = len(dna_strings)
    m = len(dna_strings[0])
    profile_matrix = {
        'A': [None] * m,
        'C': [None] * m,
        'G': [None] * m,
        'T': [None] * m,
    }

    for i in range(0, m):
        countA = 0
        countC = 0
        countG = 0
        countT = 0
        for j in range(0, n):
            if (dna_strings[j][i] == 'A'):
                countA += 1
            elif (dna_strings[j][i] == 'C'):
                countC += 1
            elif (dna_strings[j][i] == 'G'):
                countG += 1
            elif (dna_strings[j][i] == 'T'):
                countT += 1
        profile_matrix['A'][i] = countA
        profile_matrix['C'][i] = countC
        profile_matrix['G'][i] = countG
        profile_matrix['T'][i] = countT

    return profile_matrix


def createConsensusString(P):
    m = len(P['A'])
    consensus_string = ""

    for i in range(0, m):
        genomes = ['A', 'C', 'G', 'T']
        counts = [P['A'][i], P['C'][i], P['G'][i], P['T'][i]]
        max_index = counts.index(max(counts))
        consensus_string += genomes[max_index]

    return consensus_string


def main():
    # Get multiline input
    lines = sys.stdin.readlines()
    dna_strings = sortInput(lines)
    P = createProfileMatrix(dna_strings)
    C = createConsensusString(P)

    print(C)
    for key, value in P.items():
        print(str(key) + ":", *value)


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
