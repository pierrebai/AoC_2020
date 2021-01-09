def input():
    adapter_jolts = list(map(int, filter(None, open('day_10/input.txt').read().split('\n'))))
    adapter_jolts.sort()
    adapter_jolts.insert(0, 0)
    adapter_jolts.append(adapter_jolts[-1] + 3)
    return adapter_jolts

def part_1(adapter_jolts):
    adapter_diffs = list(map(lambda ab: ab[1] - ab[0], zip(adapter_jolts[0:-1], adapter_jolts[1:])))
    one_diffs = list(filter(lambda x: x == 1, adapter_diffs))
    three_diffs = list(filter(lambda x: x == 3, adapter_diffs))
    return len(one_diffs) * len(three_diffs)

def part_2(adapter_jolts):
    reach_counts = [1]
    for index in range(1, len(adapter_jolts)):
        index_reach_count = 0
        for reach in range(index -1, -1, -1):
            if adapter_jolts[index] - adapter_jolts[reach] > 3:
                break
            index_reach_count += reach_counts[reach]
        reach_counts.append(index_reach_count)

    return reach_counts[-1]

if __name__ == '__main__':
    print(part_1(input()))
    print(part_2(input()))
