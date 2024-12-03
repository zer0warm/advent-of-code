def compute_distance(a: list, b: list) -> int:
    return sum([abs(i - j) for i, j in zip(sorted(a), sorted(b))])

def compute_similarity(a: list, b: list) -> int:
    return sum([i * b.count(i) for i in a])

if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()

    pairs = [tuple(map(int, line.split())) for line in lines]
    left = [p[0] for p in pairs]
    right = [p[1] for p in pairs]

    print('Part 1:', compute_distance(left, right))
    print('Part 2:', compute_similarity(left, right))
