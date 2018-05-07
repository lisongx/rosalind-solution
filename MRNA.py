# http://rosalind.info/problems/mrna/

import sys

code_map = {
    'UUU': 'F',
    'CUU': 'L',
    'AUU': 'I',
    'UUC': 'F',
    'CUC': 'L',
    'AUC': 'I',
    'UUA': 'L',
    'CUA': 'L',
    'AUA': 'I',
    'UUG': 'L',
    'CUG': 'L',
    'AUG': 'M',
    'UCU': 'S',
    'CCU': 'P',
    'ACU': 'T',
    'UCC': 'S',
    'CCC': 'P',
    'ACC': 'T',
    'UCA': 'S',
    'CCA': 'P',
    'ACA': 'T',
    'UCG': 'S',
    'CCG': 'P',
    'ACG': 'T',
    'UAU': 'Y',
    'CAU': 'H',
    'AAU': 'N',
    'UAC': 'Y',
    'CAC': 'H',
    'AAC': 'N',
    'UAA': 'Stop',
    'CAA': 'Q',
    'AAA': 'K',
    'UAG': 'Stop',
    'CAG': 'Q',
    'AAG': 'K',
    'UGU': 'C',
    'CGU': 'R',
    'AGU': 'S',
    'UGC': 'C',
    'CGC': 'R',
    'AGC': 'S',
    'UGA': 'Stop',
    'CGA': 'R',
    'AGA': 'R',
    'UGG': 'W',
    'CGG': 'R',
    'AGG': 'R',
    'GUU': 'V',
    'GUC': 'V',
    'GUA': 'V',
    'GUG': 'V',
    'GCU': 'A',
    'GCC': 'A',
    'GCA': 'A',
    'GCG': 'A',
    'GAU': 'D',
    'GAC': 'D',
    'GAA': 'E',
    'GAG': 'E',
    'GGU': 'G',
    'GGC': 'G',
    'GGA': 'G',
    'GGG': 'G',
}


MODULO = 1000000


def get_num(dna_str):
    results_number = []
    count_by_c = {}
    for k, v in code_map.iteritems():
        if v not in count_by_c:
            count_by_c[v] = 1
        else:
            count_by_c[v] += 1
    total = count_by_c['Stop']
    for i in dna_str:
        total *= count_by_c[i]
        total = total % MODULO
    return total % MODULO


def main():
    input = read_input()
    c = get_num(input)
    print(c)


def read_input():
    input = sys.argv[1]
    return open(input).read().strip()


if __name__ == '__main__':
    main()
