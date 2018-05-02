# http://rosalind.info/problems/iprb/
# recursive one

import sys


def get_permutation(n):
    combs = []
    input_list = list(range(1, n + 1))
    def cal(items):
        if len(items) <= 1:
            return [items]
        else:
            selected = items[0]
            rest = items[1:]
            pems = cal(rest)
            res = []
            for pem in pems:
                for i in range(0, len(pem) + 1):
                    r = pem[:i] + [selected] + pem[i:]
                    res.append(r)
            return res
    return cal(input_list)


def main():
    input = read_input()
    n = int(input)
    combs = get_permutation(n)
    print(len(combs))
    for c in combs:
        print(' '.join(map(str, c)))


def read_input():
    input = sys.argv[1]
    return open(input).read().strip()


if __name__ == '__main__':
    main()
