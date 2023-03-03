# 21) Open Reading Frames
import sys
import os

DNA_CODON_TABLE = {
    'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': '-',     'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': '-',     'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': '-',     'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}


def sortInput(lines):
    dna_string = ""
    for i in range(1, len(lines)):
        dna_string += lines[i].strip()
    return dna_string


def reverseCompliment(str):
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


def translateToProtein(str):
    protein_str = ""
    for i in range(0, len(str), 3):
        codon = str[i:i+3]
        if (codon not in DNA_CODON_TABLE):
            return

        symbol = DNA_CODON_TABLE[codon]
        if (symbol == "-"):
            return protein_str
        protein_str += symbol

    return


def candidateProteinStrings(dna):
    candidate_strings = []
    # Calculate positions of start and end codons #
    start_positions = []

    for i in range(0, len(dna)):
        codon = dna[i:i+3]
        symbol = DNA_CODON_TABLE[codon] if (codon in DNA_CODON_TABLE) else None
        if (symbol == 'M'):
            start_positions.append(i)

    for i in start_positions:
        str = translateToProtein(dna[i:])
        if (str is not None):
            candidate_strings.append(str)

    return candidate_strings


def main():
    lines = sys.stdin.readlines()
    dna_string = sortInput(lines)
    candidate_strings = candidateProteinStrings(
        dna_string) + candidateProteinStrings(reverseCompliment(dna_string))
    [print(str) for str in set(candidate_strings)]


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
