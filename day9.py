import re


doPartB = True


marker = re.compile('^\((\d+)x(\d+)\)')


def is_marker(s: str) -> bool:
    return marker.match(s) is not None


def get_marker_length(m: str) -> bool:
    return m.index(')') + 1


def get_marker_params(m: str) -> str:
    return marker.match(m).groups()


def decompress(file: str) -> str:
    index = 0
    result = ''
    while index < len(file):
        if is_marker(file[index:]):
            params = get_marker_params(file[index:])
            data_length = int(params[0])
            repeats = int(params[1])
            marker_length = get_marker_length(file[index:])
            if doPartB:
                # Won't actually work; TOO MUCH STRING HALP
                data = decompress(file[index + marker_length:index + marker_length + data_length])
            else:
                data = file[index + marker_length:index + marker_length + data_length]
            result += data * repeats
            index += marker_length + data_length
        else:
            result += file[index]
            index += 1

    return result


def decompressed_length(file: str) -> str:
    length = 0
    index = 0
    while index < len(file):
        if is_marker(file[index:]):
            params = get_marker_params(file[index:])
            data_length = int(params[0])
            repeats = int(params[1])
            marker_length = get_marker_length(file[index:])
            if doPartB:
                length += decompressed_length(file[index + marker_length:index + marker_length + data_length]) * repeats

            else:
                length += data_length * repeats
            index += marker_length + data_length
        else:
            length += 1
            index += 1

    return length


with open('inputs/day9.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

for line in lines:
    print("Decompressed length: " + str(decompressed_length(line)))


