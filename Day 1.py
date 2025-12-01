class PartOne:
    def turn_left(self, position, by:int):
        position -= by
        if position < 0:
            position %= 100
        return position

    def turn_right(self, position, by:int):
        position += by
        if position >=100:
            position %= 100
        return position

    def solve(self, filename: str="input.txt"):
        position = 50
        zero = 0

        with open(filename, "r") as file:
            d = file.read()

        for line in d.split("\n")[:-1]:
            if line[0] == "L":
                position = self.turn_left(position, int(line[1:]))
            if line[0] == "R":
                position = self.turn_right(position, int(line[1:]))
            if position == 0:
                zero += 1

        print(f"Number of zeros: {zero}")


class PartTwo:
    def solve(self, filename: str = "input.txt"):
        position = 50
        zero_count = 0

        with open(filename, "r") as file:
            d = file.read()

        for line in d.split("\n"):
            if not line:
                continue

            direction = line[0]
            distance = int(line[1:])
            zeros_this_turn = 0

            if direction == "L":
                zeros_this_turn += distance // 100
                remaining_dist = distance % 100
                if position > 0 and position - remaining_dist <= 0:
                    zeros_this_turn += 1
                elif position == 0 and distance > 0:
                    pass

                position = (position - distance) % 100
            elif direction == "R":
                zeros_this_turn += distance // 100
                remaining_dist = distance % 100
                if position + remaining_dist >= 100:
                    zeros_this_turn += 1

                position = (position + distance) % 100

            zero_count += zeros_this_turn
        print(f"Part Two Answer: {zero_count}")
        return zero_count


if __name__ == "__main__":
    print("Running Part One...")
    part_one = PartOne()
    part_one.solve()

    print("\nRunning Part Two...")
    part_two = PartTwo()
    part_two.solve(filename="input.txt")
