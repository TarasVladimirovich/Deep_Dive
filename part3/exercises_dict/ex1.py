from collections import defaultdict, Counter

d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}
d4 = {'modula-2': 100}


def merge(*dicts):
    unsorted = {}
    for d in dicts:
        for k, v in d.items():
            unsorted[k] = unsorted.get(k, 0) + v

    # create a dictionary sorted by value
    return dict(sorted(unsorted.items(), key=lambda e: e[1], reverse=True))


print(merge(d1, d2, d3))


def merge_default(*dicts):
    unsorted = defaultdict(int)
    for d in dicts:
        for k, v in d.items():
            unsorted[k] += v

    # create a dictionary sorted by value
    return dict(sorted(unsorted.items(), key=lambda e: e[1], reverse=True))


print(merge_default(d1, d2, d3))


def merge_counter(*dicts):
    unsorted = Counter()
    for d in dicts:
        unsorted.update(d)

    return dict(unsorted.most_common())


print(merge_counter(d1, d2, d3))
