# http://rosalind.info/problems/fibd/

import sys


CACHED_G = {}


def g(n, m):
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    elif n in CACHED_G:
        return CACHED_G[n]
    elif n <= m:
        res = g(n - 1, m) + g(n - 2, m)
    elif n == m + 1:
        res = g(n - 1, m) + g(n - 2, m) - 1
    else:
        res = g(n - 1, m) + g(n - 2, m) - g(n - (m + 1), m)
    CACHED_G[n] = res
    return res



def main():
    input = read_input()
    n, m = map(int, input.split(' '))
    print(g(n, m))


def read_input():
    input = sys.argv[1]
    return open(input).read().strip()


if __name__ == '__main__':
    main()
