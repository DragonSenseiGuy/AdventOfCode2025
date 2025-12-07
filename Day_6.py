from collections import defaultdict
import math
from math import prod

class PartOne:
    def solve(self):
        data = open("input.txt", "r").read().splitlines()

        operations = defaultdict(list)

        for i in range(len(data)):
            numbers = data[i].strip().split(" ")
            numbers = [number for number in numbers if len(number) != 0]

            for j in range(len(numbers)):
                operations[j].append(numbers[j])

        solution = 0
        for i, operation in operations.items():
            operator = operation[-1]
            operants = operation[:-1]
            operants = [int(i) for i in operants]

            if operator == "*":
                solution += math.prod(operants)
            elif operator == "+":
                solution += sum(operants)

        print(f"Solution part 1: {solution}")

class PartTwo:
    def solve(self):
        with open("input.txt", "r") as f:
            data = f.read().splitlines()

        # 1. Pad input into a rectangular grid
        height = len(data)
        width = max(len(line) for line in data) if data else 0
        grid = [line.ljust(width) for line in data]

        # 2. Identify problem boundaries based on all-space columns
        problem_splits = [-1]
        for c in range(width):
            if all(grid[r][c] == ' ' for r in range(height)):
                problem_splits.append(c)
        problem_splits.append(width)
        
        problem_grids = []
        for i in range(len(problem_splits) - 1):
            start = problem_splits[i] + 1
            end = problem_splits[i+1]
            if start >= end:
                continue
            
            problem_grid = [row[start:end] for row in grid]
            problem_grids.append(problem_grid)

        # 3. Process problems right to left
        grand_total = 0
        for problem_grid in reversed(problem_grids):
            operator_line = problem_grid[-1]
            operator = "".join(operator_line.split())
            
            number_grid_rows = problem_grid[:-1]
            if not number_grid_rows:
                continue
            
            problem_width = len(number_grid_rows[0])
            new_operands_str = []
            for c in range(problem_width):
                vertical_slice = "".join(row[c] for row in number_grid_rows)
                num_str = vertical_slice.strip()
                if num_str:
                    new_operands_str.append(num_str)
            
            operands = [int(s) for s in new_operands_str]

            # 4. Calculate result for the problem
            result = 0
            if operator == '+':
                result = sum(operands)
            elif operator == '*':
                result = math.prod(operands)
            
            grand_total += result
            
        print(f"Solution part 2: {grand_total}")


if __name__ == "__main__":
    part_one = PartOne()
    part_one.solve()

    part_two = PartTwo()
    part_two.solve()

