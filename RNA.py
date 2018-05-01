import sys


def process(dna_str):
    n = ['U' if d == 'T' else d for d in dna_str]
    print(''.join(n))


def main():
    input = read_input()
    process(input)


def read_input():
    input = sys.argv[1]
    return open(input).read()


if __name__ == '__main__':
    main()
