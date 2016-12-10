from typing import List, Tuple


def get_instructions(instructions: str) -> List[Tuple]:
    return [(instruction[0], int(instruction[1:])) for instruction in instructions.split(', ')]


class Walker(object):

    def __init__(self, x: int = 0, y: int = 0):
        self.visited = set()
        self.first_duplicate = None
        self.orientation = 'N'
        self.x = x
        self.y = y
        self.update_visited()

    def update_visited(self):
        if (self.x, self.y) in self.visited:
            if self.first_duplicate is None:
                self.first_duplicate = (self.x, self.y)
        else:
            self.visited.add((self.x, self.y))

    def change_orientation(self, direction: str) -> None:
        if self.orientation == 'N':
            if direction == 'L':
                self.orientation = 'W'
            elif direction == 'R':
                self.orientation = 'E'
        elif self.orientation == 'E':
            if direction == 'L':
                self.orientation = 'N'
            elif direction == 'R':
                self.orientation = 'S'
        elif self.orientation == 'S':
            if direction == 'L':
                self.orientation = 'E'
            elif direction == 'R':
                self.orientation = 'W'
        elif self.orientation == 'W':
            if direction == 'L':
                self.orientation = 'S'
            elif direction == 'R':
                self.orientation = 'N'

    def move_increment(self):
        if self.orientation == 'N':
            self.y += 1
        elif self.orientation == 'E':
            self.x += 1
        elif self.orientation == 'S':
            self.y -= 1
        elif self.orientation == 'W':
            self.x -= 1
        self.update_visited()

    def move_straight(self, distance: int) -> None:
        for i in range(distance):
            self.move_increment()

    def move(self, direction: str, distance: int) -> None:
        self.change_orientation(direction)
        self.move_straight(distance)

    def follow_instructions(self, instructions: List[Tuple]) -> None:
        for instruction in instructions:
            self.move(instruction[0], instruction[1])

    def distance(self, x: int, y: int) -> int:
        # Distance is 'taxicab distance'
        return abs((self.x - x)) + abs((self.y - y))

    def distance_from_origin(self, x: int, y: int) -> int:
        # Distance is 'taxicab distance'
        return abs(x) + abs(y)

    def first_duplicate_distance(self) -> int:
        return self.distance_from_origin(self.first_duplicate[0], self.first_duplicate[1])


if __name__ == '__main__':
    with open('inputs/day1.txt', 'r') as f:
        instructions = f.readline()

    walker = Walker(0, 0)
    walker.follow_instructions(get_instructions(instructions))

    print("Total Distance: " + str(walker.distance(0, 0)))
    print("Distance to first location visited twice: " + str(walker.first_duplicate_distance()))
