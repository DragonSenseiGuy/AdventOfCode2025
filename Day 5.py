class PartOne:
    def solve(self, filename="input.txt"):
        range_strings = []
        id_strings = []
        with open(filename) as f:
            # Read all non-empty lines from the file
            stripped_list = [s.strip() for s in f.readlines() if s.strip()]

        # Separate range strings from ID strings
        for item in stripped_list:
            if "-" in item:
                range_strings.append(item)
            else:
                id_strings.append(item)

        # Convert range strings into integer tuples (start, end)
        fresh_ranges = []
        for r_str in range_strings:
            start, end = r_str.split('-')
            fresh_ranges.append((int(start), int(end)))

        # Convert ID strings to a list of integers
        available_ids = [int(id_str) for id_str in id_strings]

        # Check each available ID to see if it falls into any fresh range
        fresh_count = 0
        for an_id in available_ids:
            is_id_fresh = False
            for start, end in fresh_ranges:
                if start <= an_id <= end:
                    is_id_fresh = True
                    break  # The ID is fresh, no need to check other ranges
            if is_id_fresh:
                fresh_count += 1

        print(f"Number of fresh ingredients: {fresh_count}")


class PartTwo:
    def solve(self, filename="input.txt"):
        range_strings = []
        with open(filename) as f:
            for line in f:
                line = line.strip()
                if not line:
                    # The blank line separates the ranges from the other data
                    break
                if "-" in line:
                    range_strings.append(line)

        if not range_strings:
            print("Total number of fresh ingredient IDs: 0")
            return

        # Parse range strings into integer tuples
        ranges = []
        for r_str in range_strings:
            start, end = r_str.split('-')
            ranges.append((int(start), int(end)))

        # Sort ranges based on their starting value
        ranges.sort(key=lambda x: x[0])

        # Merge overlapping ranges
        merged_ranges = []
        merged_ranges.append(list(ranges[0]))

        for i in range(1, len(ranges)):
            current_start, current_end = ranges[i]
            last_start, last_end = merged_ranges[-1]

            if current_start <= last_end:
                # There is an overlap, so merge the current range
                merged_ranges[-1][1] = max(last_end, current_end)
            else:
                # No overlap, add the new range
                merged_ranges.append(list(ranges[i]))

        # Calculate the total number of IDs from the merged ranges
        total_fresh_ids = 0
        for start, end in merged_ranges:
            total_fresh_ids += (end - start + 1)

        print(f"Total number of fresh ingredient IDs: {total_fresh_ids}")


if __name__ == '__main__':
    print("Running Part One...")
    part_one = PartOne()
    part_one.solve()

    print("\nRunning Part Two...")
    part_two = PartTwo()
    part_two.solve()