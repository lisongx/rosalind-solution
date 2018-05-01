import sys

def d_hamming(l1, l2):
    d = 0
    for c1, c2 in zip(l1, l2):
        if c1 != c2:
            d += 1
    return d


def main():
    input = read_input()
    lines = input.splitlines()
    l1, l2 = lines
    print(d_hamming(l1.strip(), l2.strip()))


def read_input():
    input = sys.argv[1]
    return open(input).read().strip()


if __name__ == '__main__':
    main()
