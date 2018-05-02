# http://rosalind.info/problems/subs/

import sys


def get_sub_indexs(dna_str, t):
    indexs = []
    motif_len = len(t)

    for index, d in enumerate(dna_str):
        if dna_str[index:index+motif_len] == t:
            indexs.append(index + 1)
    return indexs


def main():
    input = read_input()
    dna_str, t = input.splitlines()
    indexs = get_sub_indexs(dna_str, t)
    print(' '.join(map(str, indexs)))


def read_input():
    input = sys.argv[1]
    return open(input).read().strip()


if __name__ == '__main__':
    main()
