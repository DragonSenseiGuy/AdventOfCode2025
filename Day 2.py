class PartOne:
    def check_id(self, split_content):
        duplicate_count = 0
        for id in split_content:
            split_list = id.split("-")
            first_part = split_list[0]
            second_part = split_list[1]
            for num in range(int(first_part), int(second_part) + 1):
                num =  str(num)
                string_middle = len(num) // 2
                string_first_part = num[:string_middle]
                string_second_part = num[string_middle:]
                if string_first_part == string_second_part:
                    duplicate_count+=int(num)
        print(f"Part One Answer: {duplicate_count}")
        return duplicate_count

    def solve(self, filename="input.txt"):
        with open(filename, "r") as file:
            content = file.read()
            split_content = content.strip().split(",")
        self.check_id(split_content)


class PartTwo:
    def is_invalid(self, num: int) -> bool:
        s = str(num)
        L = len(s)
        for p_len in range(1, L // 2 + 1):
            if L % p_len == 0:
                pattern = s[:p_len]
                repetitions = L // p_len
                if repetitions >= 2:
                    if pattern * repetitions == s:
                        return True
        return False

    def check_id(self, split_content):
        invalid_id_sum = 0
        for id_range in split_content:
            if not id_range:
                continue
            split_list = id_range.split("-")
            start = int(split_list[0])
            end = int(split_list[1])
            for num in range(start, end + 1):
                if self.is_invalid(num):
                    invalid_id_sum += num
        print(f"Part Two Answer: {invalid_id_sum}")
        return invalid_id_sum

    def solve(self, filename="input.txt"):
        with open(filename, "r") as file:
            content = file.read()
            split_content = content.strip().split(",")
        self.check_id(split_content)


if __name__ == "__main__":
    print("Running Part One...")
    part_one = PartOne()
    part_one.solve()

    print("\nRunning Part Two...")
    part_two = PartTwo()
    part_two.solve()