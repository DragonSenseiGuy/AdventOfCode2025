bank = []

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]

with open('input.txt') as f:
    lines = [line.rstrip('\r\n') for line in f]
bank = [list(line) for line in lines]

rolls = 0
grid_height = len(bank)
grid_width = len(bank[0])


def calculate_rolls():
    global rolls
    for r, row in enumerate(bank):
        for c, char in enumerate(row):
            if char != '@':
                continue

            adjacent_rolls = 0

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if (0 <= nr < grid_height and
                        0 <= nc < grid_width and
                        bank[nr][nc] == '@'):
                    adjacent_rolls += 1
            if adjacent_rolls < 4:
                rolls += 1
                bank[r][c] = '.'


while True:
    calculate_rolls()
    print(rolls)