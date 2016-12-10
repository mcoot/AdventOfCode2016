from math import inf

doPartB = True


def transpose(l):
    return [list(i) for i in zip(*l)]


def count_frequencies(l):
    seen = {}
    for element in l:
        seen[element] = seen.get(element, 0) + 1
    return seen


def most_frequent(l):
    seen = count_frequencies(l)

    mf = None
    mval = 0
    for key in seen:
        if seen[key] > mval:
            mf = key
            mval = seen[key]

    return mf


def least_frequent(l):
    seen = count_frequencies(l)

    mf = None
    mval = inf
    for key in seen:
        if seen[key] < mval:
            mf = key
            mval = seen[key]

    return mf


def recreate_message(l):
    result = ''
    for column in l:
        if doPartB:
            result += least_frequent(column)
        else:
            result += most_frequent(column)

    return result


with open('inputs/day6.txt', 'r') as f:
    lines = f.readlines()

print(transpose(lines))
print("Message: " + recreate_message(transpose(lines)))
