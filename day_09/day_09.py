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

input_data = list(map(int, filter(None, open('day_09/input.txt').read().split('\n'))))

target = find_not_matching_pool(input_data[0:25], input_data[25:])
print(str(target))


def find_matching_range(target, values):
    for start in range(0, len(values)):
        total = values[start]
        for end in range(start+1, len(values)):
            total += values[end]
            if total == target:
                return values[start:end+1]
            if total > target:
                break

interval = find_matching_range(target, input_data)
print(str(min(interval) + max(interval)))


