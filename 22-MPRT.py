# 22) Finding a Protein Motif
import sys
import os
import re
from urllib.request import urlopen
from urllib.error import URLError


def getData(uniprot_id):
    data = None
    try:
        with urlopen(f'http://www.uniprot.org/uniprot/{uniprot_id}.fasta') as f:
            data = f.readlines()
    except URLError as err:
        print(err.reason)
    return data


class prot_obj:
    def __init__(self, id, str):
        self.id = id
        self.str = str
        self.locations = findProteinMotif(str)


def sortUrlInput(uniprot_ids):
    protein_data = []
    for id in uniprot_ids:
        str = ""
        data = getData(id[:6].strip())  # valid UniProtKB is of type 'B5ZC00'

        if (data is not None):
            for i in range(1, len(data)):
                str += data[i].decode('utf-8')
            protein_data.append(prot_obj(id, str))

    return protein_data


def sortFastaInput(lines):
    protein_data = []

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

            dna = prot_obj(id[1:], str)
            protein_data.append(dna)
    return protein_data


def findProteinMotif(protein):
    locations = []
    for i in range(0, len(protein)):
        if (re.match('^N[^P][ST][^P]$', protein[i:i+4])):
            locations.append(i+1)
    return locations


def main():
    lines = sys.stdin.readlines()
    protein_data = sortFastaInput(lines)
    for x in protein_data:
        if (x.locations):
            print(x.id.strip())
            print(*x.locations)


if __name__ == '__main__':
    if not os.environ.get("ONLINE_JUDGE"):
        sys.stdin = open('./input.txt', 'r')
        sys.stdout = open('./output.txt', 'w')
    main()
