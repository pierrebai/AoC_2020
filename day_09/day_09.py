def input():
    return list(map(int, filter(None, open('day_09/input.txt').read().split('\n'))))

def is_sum_of_two_in_pool(v, pool):
    for v1 in pool:
        for v2 in pool:
            if v1 == v2:
                continue
            if v == v1 + v2:
                return True
    return False

def find_not_matching_pool(pool, to_verify):
    insertion_point = 0
    for v in to_verify:
        if not is_sum_of_two_in_pool(v, pool):
            return v
        pool[insertion_point] = v
        insertion_point = (insertion_point + 1) % len(pool)
    return "All numbers match."

def part_1(input_data):
    return find_not_matching_pool(input_data[0:25], input_data[25:])

def find_matching_range(target, values):
    for start in range(0, len(values)):
        total = values[start]
        for end in range(start+1, len(values)):
            total += values[end]
            if total == target:
                return values[start:end+1]
            if total > target:
                break

def part_2(input_data):
    target = find_not_matching_pool(input_data[0:25], input_data[25:])
    interval = find_matching_range(target, input_data)
    return min(interval) + max(interval)

if __name__ == '__main__':
    print(part_1(input()))
    print(part_2(input()))

