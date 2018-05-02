# http://rosalind.info/problems/iprb/

import sys

p_cfgs = [1, 0.5, 0]


def get_p(homo_domi, heter, homo_rece):
    args = [homo_domi, heter, homo_rece]
    total = sum(args)
    indexs = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
    p = 0
    for n1, n2 in indexs:
        j = args[n1]
        k = args[n2]
        r1 = p_cfgs[n1]
        r2 = p_cfgs[n2]
        p_for_r = 1 - (1 - r1) * (1 - r2)
        if n1 == n2:
            p1 = (j/total * (j-1)/(total - 1)) * p_for_r
            p = p + p1
        else:
            p1 = (j/total * k/(total-1)) * p_for_r
            p2 = (k/total * j/(total-1)) * p_for_r
            p = p + (p1 + p2)
    return p


def main():
    input = read_input()
    k, m, n = map(int, input.split(' '))
    p = get_p(k, m, n)
    print(p)


def read_input():
    input = sys.argv[1]
    return open(input).read().strip()


if __name__ == '__main__':
    main()
