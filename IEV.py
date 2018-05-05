# http://rosalind.info/problems/iev/

import sys



def get_p(ns):
    assert len(ns) == 6
    ps = [1, 1, 1, 0.75, 0.5, 0]
    pros = sum([2*n*ps for n, ps in zip(ns, ps)])
    return pros


def main():
    input = read_input()
    ns = list(map(int, input.split(' ')))
    print(get_p(ns))


def read_input():
    input = sys.argv[1]
    return open(input).read().strip()



if __name__ == '__main__':
    main()
