from hashlib import md5
import time


doPartB = True


def get_hash(room_index: str) -> str:
    return md5(room_index.encode()).hexdigest()


def check_hash(h: str) -> bool:
    for i in range(5):
        if h[i] != '0':
            return False
    return True


def get_next_character(h: str):
    return h[5]


def update_password(password: str, h: str):
    if doPartB:
        i = h[5]
        if h[5] in '01234567' and password[int(h[5])] == 'x':
            return password[:int(i)] + h[6] + password[int(i)+1:]
        else:
            return password
    else:
        i = password.index('x')
        return password[:i] + h[5] + password[i+1:]


def find_password(room_id: str):
    index = 0
    found = 0
    password = 'xxxxxxxx'
    while 'x' in password:
        h = get_hash(room_id + str(index))
        if check_hash(h):
            password = update_password(password, h)
            print('#%d: %s' % (index, password))
        index += 1

    return password


with open('inputs/day5.txt', 'r') as f:
    door_id = f.readline().strip()

startTime = time.time()
pw = find_password(door_id)
endTime = time.time()

print("Password for %s: %s [decrypted in %f seconds]" % (door_id, pw, endTime - startTime))
