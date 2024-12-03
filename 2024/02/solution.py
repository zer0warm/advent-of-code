def get_trend_func(L):
    if L[0] < L[1]:
        return lambda a, b: a < b
    elif L[0] > L[1]:
        return lambda a, b: a > b
    return lambda a, b: False

def within_range(a, b):
    return 1 <= abs(a - b) <= 3

def is_safe(levels):
    pairs = list(zip(levels[:-1], levels[1:]))
    same_trend = get_trend_func(levels)
    return (all(map(lambda p: same_trend(*p), pairs[1:])) and
            all(map(lambda p: within_range(*p), pairs)))

def count_safe_reports(reports):
    return len(list(filter(is_safe, reports)))

def dampen_unsafe(levels):
    return any([is_safe(levels[:i] + levels[i+1:])
                for i in range(len(levels))])

def count_safe_reports2(reports):
    unsafe = filter(lambda r: not is_safe(r), reports)
    new_safe = list(filter(dampen_unsafe, unsafe))
    return count_safe_reports(reports) + len(new_safe)

def convert_int(report):
    return list(map(int, report.split()))

if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()

    reports = list(map(convert_int, lines))
    print("Part 1:", count_safe_reports(reports))
    print("Part 2:", count_safe_reports2(reports))
