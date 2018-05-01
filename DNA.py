import sys


def count_dna(dna_str):
    cnt_char = ['A', 'C', 'G', 'T']
    cnt = {}
    for c in dna_str:
        if c in cnt:
            cnt[c] += 1
        else:
            cnt[c] = 1
    res = [str(cnt[c]) for c in cnt_char]
    print(' '.join(res))


def main():
    input = read_input()
    count_dna(input)


def read_input():
    input = sys.argv[1]
    return open(input).read()


if __name__ == '__main__':
    main()
