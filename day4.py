from typing import List
from queue import PriorityQueue


def calculate_checksum(room: str, length: int) -> str:
    frequencies = dict()
    for letter in room.split('[')[0].lower():
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            frequencies[letter] = frequencies.get(letter, 0) + 1
    pq = PriorityQueue()
    for key, val in frequencies.items():
        pq.put((-val, key))

    checksum = ''
    for i in range(min(length, len(frequencies))):
        checksum += pq.get()[1]

    return checksum


def decrypt(text: str, key: int) -> str:
    key %= 26
    return ''.join([chr((((ord(c) - ord('a')) + key) % 26) + ord('a')) if c in 'abcdefghijklmnopqrstuvwxyz' else c
                    for c in text])


def extract_name(room:str) -> str:
    endname = room.split('[')[0].rfind('-')
    return room[:endname].replace('-', ' ')


def extract_checksum(room: str) -> str:
    return room.split('[')[1][:5]


def extract_sector_id(room: str) -> int:
    return int(room.split('[')[0].split('-')[-1])


def is_real(room: str) -> bool:
    return calculate_checksum(room, 5) == extract_checksum(room)


def sum_real_sector_ids(rooms: List[str]) -> int:
    count = 0
    for room in rooms:
        if is_real(room):
            count += extract_sector_id(room)
    return count


def decrypt_names(rooms: List[str]) -> List[str]:
    return [decrypt(extract_name(room), extract_sector_id(room)) for room in rooms]


with open('inputs/day4.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]


real_lines = [line for line in lines if is_real(line)]
print('Sum of real sector IDs: ' + str(sum_real_sector_ids(lines)))

decrypted = decrypt_names(real_lines)

for i in range(len(real_lines)):
    print("{0} = {1} (Sector {2})".format(real_lines[i], decrypted[i], extract_sector_id(real_lines[i])))
