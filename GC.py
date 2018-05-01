import sys


def gc_content(dna_str):
    total = 0
    hit = 0
    for d in dna_str:
        if d in ['G', 'C']:
            hit += 1
        total += 1
    return hit, total


def main():
    input = read_input()
    lines = input.splitlines()
    data = []
    hit, total = 0, 0
    dna_id = None
    for index, l in enumerate(lines):
        if l.startswith('>'):
            if dna_id is not None:
                assert total > 0
                data.append(
                    (dna_id, hit*1.0 / total)
                )
                total = 0
                hit = 0

            dna_id = l.strip()[1:]
        else:
            hit_, total_ = gc_content(l.strip())
            hit += hit_
            total += total_
    data.append(
        (dna_id, hit*1.0 / total)
    )
    res = sorted(data, key=lambda l: l[1], reverse=True)[0]
    print(res[0])
    print(res[1] * 100)


def read_input():
    input = sys.argv[1]
    return open(input).read().strip()


if __name__ == '__main__':
    main()
