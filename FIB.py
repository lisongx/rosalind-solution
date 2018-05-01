import sys


global CACHED

CACHED = {}

def f(n, k):
    if n <= 2:
        return 1
    elif n in CACHED:
        return CACHED[n]
    else:
        res = f(n - 1, k) + k * f(n - 2, k)
        CACHED[n] = res
        return res


def main():
    input = read_input()
    n, k = map(int, input.split(' '))
    print(f(n, k))


def read_input():
    input = sys.argv[1]
    return open(input).read().strip()


if __name__ == '__main__':
    main()
