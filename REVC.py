import sys

_map = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C',
}

def process(dna_str):
    n = [_map[d] for d in dna_str[::-1]]
    print(''.join(n))


def main():
    input = read_input()
    process(input)


def read_input():
    input = sys.argv[1]
    return open(input).read().strip()


if __name__ == '__main__':
    main()
