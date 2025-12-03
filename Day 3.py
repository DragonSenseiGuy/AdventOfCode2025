class PartOne:
    def solve(self, filename="input.txt"):
        total_joltage = 0
        with open(filename, "r") as file:
            lines = file.read().splitlines()

        for line in lines:
            if not line:
                continue

            max_for_line = 0
            n = len(line)
            if n < 2:
                continue

            for i in range(n):
                for j in range(i + 1, n):
                    num = int(line[i] + line[j])
                    if num > max_for_line:
                        max_for_line = num
            total_joltage += max_for_line

        print(total_joltage)

class PartTwo:
    def find_largest_number(self, digits: str, length: int) -> int:
        n = len(digits)
        if n <= length:
            return int(digits)

        k_to_remove = n - length
        stack = []

        for digit in digits:
            while stack and digit > stack[-1] and k_to_remove > 0:
                stack.pop()
                k_to_remove -= 1
            stack.append(digit)

        final_stack = stack[:length]

        return int("".join(final_stack))

    def solve(self, filename="input.txt"):
        total_joltage = 0
        with open(filename, "r") as file:
            lines = file.read().splitlines()

        for line in lines:
            if not line:
                continue

            total_joltage += self.find_largest_number(line, 12)

        print(f"Part Two Answer: {total_joltage}")


if __name__ == "__main__":
    print("Running Part One...")
    part_one = PartOne()
    part_one.solve()

    print("\nRunning Part Two...")
    part_two = PartTwo()
    part_two.solve()