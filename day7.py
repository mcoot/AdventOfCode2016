from typing import List
import re


def is_abba(s: str) -> bool:
    return s[0] == s[3] and s[1] == s[2] and s[0] != s[1]


def has_abba(s: str) -> bool:
    return any([is_abba(s[sub:sub+4])
                for sub
                in range(len(s) - 3)])


def is_aba(s: str) -> bool:
    return s[0] == s[2] and s[0] != s[1]


def has_bab(s: str, aba: str):
    return any([is_aba(s[sub:sub+3]) and s[sub:sub+3][0] == aba[1] and s[sub:sub+3][1] == aba[0]
                for sub
                in range(len(s) - 2)])


def get_abas(s: str):
    return filter(is_aba, [s[sub:sub+3] for sub in range(len(s) - 2)])


def get_non_hypernets(address: str) -> List[str]:
    segments = re.split("[\[\]]", address)
    return segments[::2]


def get_hypernets(address: str) -> List[str]:
    segments = re.split("[\[\]]", address)
    return segments[1::2]


with open('inputs/day7.txt', 'r') as f:
    inputs = [i.strip() for i in f.readlines()]


partA = [any([has_abba(s) for s in get_non_hypernets(address)])
          and all([not has_abba(s) for s in get_hypernets(address)])
          for address
          in inputs].count(True)

partB = [any([any([any([has_bab(s, aba)
                        for s in get_hypernets(address)])
                   for aba in get_abas(segment)])
              for segment in get_non_hypernets(address)])
         for address
         in inputs].count(True)

print("Number of TLS supporting addresses: " + str(partA))
print("Number of SSL supporting addresses: " + str(partB))
