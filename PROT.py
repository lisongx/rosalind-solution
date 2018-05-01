# http://rosalind.info/problems/prot/

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


def get_code(dna_str):
    current_cs = ''
    codes = []
    for d in dna_str:
        current_cs = current_cs + d
        if current_cs in code_map:
            c = code_map[current_cs]
            if c == 'Stop':
                break
            else:
                codes.append(c)
                current_cs = ''
    return ''.join(codes)


def main():
    input = read_input()
    c = get_code(input)
    print(c)


def read_input():
    input = sys.argv[1]
    return open(input).read().strip()


if __name__ == '__main__':
    main()
