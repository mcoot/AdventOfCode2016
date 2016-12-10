from typing import List, Tuple


class KeyPad(object):

    def __init__(self, keypad_layout: List[List[str]], start: str, invalid: str = 'x'):
        self.keypad_layout = keypad_layout
        pos = self.get_position_for_value(start)
        self.x = pos[0]
        self.y = pos[1]
        self.invalid = invalid
        self.code = ''

    def get_position_for_value(self, value: str) -> Tuple:
        x = -1
        y = -1
        for i in range(len(self.keypad_layout)):
            if value in self.keypad_layout[i]:
                y = i
                x = self.keypad_layout[i].index(value)
                break

        return x, y

    def get_value_for_position(self, x: int, y: int) -> str:
        return self.keypad_layout[y][x]

    def get_value(self) -> str:
        return self.get_value_for_position(self.x, self.y)

    def pos_after_move(self, direction: str) -> Tuple:
        if direction == 'L':
            return (self.x - 1), self.y
        elif direction == 'U':
            return self.x, (self.y - 1)
        elif direction == 'R':
            return (self.x + 1), self.y
        elif direction == 'D':
            return self.x, (self.y + 1)
        return self.x, self.y

    def can_move(self, direction: str) -> bool:
        pos = self.pos_after_move(direction)
        if pos[1] < 0 or pos[1] > len(self.keypad_layout) - 1:
            return False
        if pos[0] < 0 or pos[0] > len(self.keypad_layout[pos[1]]) - 1:
            return False
        return self.get_value_for_position(pos[0], pos[1]) != self.invalid

    def move(self, direction: str) -> None:
        if self.can_move(direction):
            pos = self.pos_after_move(direction)
            self.x = pos[0]
            self.y = pos[1]

    def move_many(self, directions: str) -> None:
        for direction in directions:
            self.move(direction)

    def enter_code(self, instructions: List[str]) -> None:
        for sequence in instructions:
            self.move_many(sequence)
            self.press()

    def press(self) -> None:
        self.code += self.get_value()


keypad_layout_normal = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

keypad_layout_actual = [
    ['x', 'x', '1', 'x', 'x'],
    ['x', '2', '3', '4', 'x'],
    ['5', '6', '7', '8', '9'],
    ['x', 'A', 'B', 'C', 'x'],
    ['x', 'x', 'D', 'x', 'x']
]

keypad = KeyPad(keypad_layout_actual, '5', 'x')

with open('inputs/day2.txt', 'r') as f:
    keypad.enter_code(f.readlines())

print("Code entered: " + keypad.code)

