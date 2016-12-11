class Screen(object):

    def __init__(self, width: int = 50, height: int = 6):
        self.width = width
        self.height = height
        self.grid = [[False for i in range(self.width)] for j in range(self.height)]

    def perform_rect(self, w: int, h: int) -> None:
        for x in range(w):
            for y in range(h):
                self.grid[y][x] = True

    def perform_rotate_row(self, y: int, n: int) -> None:
        new_row = [self.grid[y][(i-n) % self.width] for i in range(self.width)]
        self.grid[y] = new_row

    def perform_rotate_column(self, x: int, n: int) -> None:
        new_col = [self.grid[(i-n) % self.height][x] for i in range(self.height)]
        for y in range(self.height):
            self.grid[y][x] = new_col[y]

    def perform_rect_command(self, command: str) -> None:
        vals = [int(v.strip()) for v in command.replace('rect ', '').split('x')]
        self.perform_rect(vals[0], vals[1])

    def perform_rotate_row_command(self, command: str) -> None:
        vals = [int(v.strip()) for v in command.replace('rotate row y=', '').split(' by ')]
        self.perform_rotate_row(vals[0], vals[1])

    def perform_rotate_column_command(self, command: str) -> None:
        vals = [int(v.strip()) for v in command.replace('rotate column x=', '').split(' by ')]
        self.perform_rotate_column(vals[0], vals[1])

    def perform_command(self, command: str) -> None:
        if command.startswith('rect '):
            self.perform_rect_command(command)
        elif command.startswith('rotate row y='):
            self.perform_rotate_row_command(command)
        elif command.startswith('rotate column x='):
            self.perform_rotate_column_command(command)

    def count_pixels_on(self):
        return sum([self.grid[y].count(True) for y in range(self.height)])

    def __str__(self):
        return ''.join([''.join(['#' if self.grid[y][x] else '.' for x in range(self.width)]) + '\n' for y in range(self.height)])


with open('inputs/day8.txt', 'r') as f:
    instructions = [i.strip() for i in f.readlines()]

screen = Screen()
for instruction in instructions:
    screen.perform_command(instruction)
print('Number of pixels on: ' + str(screen.count_pixels_on()))
print('Final screen:\n' + str(screen))
