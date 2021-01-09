import re
from collections import defaultdict

def input():
    lines = list(filter(None, open('day_07/input.txt').read().split('\n')))
    top_bags = list(map(extract_top_bag, map(lambda x: '1 ' + x, lines)))
    sub_bags = list(map(extract_sub_bags, lines))
    bags_to_sub_bags = {
        k[1]:set(v) for k, v in zip(top_bags, sub_bags)
    }
    return bags_to_sub_bags

bag_color_re = re.compile('''([0-9]+) ([a-z ]+) bag.*''')
def extract_bag_count_and_color(s):
    m = bag_color_re.match(s.strip())
    if not m:
        return (0, None)
    return (int(m.group(1)), m.group(2))

def extract_top_bag(s):
    top_bag = s.split('contain ')[0]
    return extract_bag_count_and_color(top_bag)

def extract_sub_bags(s):
    sub_bags = s.split('contain ')[1]
    return list(map(extract_bag_count_and_color, sub_bags.split(',')))

def part_1(bags_to_sub_bags):
    container_bags = defaultdict(set)
    for parent_bag, sub_bags in bags_to_sub_bags.items():
        if sub_bags:
            for count, sub_bag in sub_bags:
                container_bags[sub_bag].add(parent_bag)

    todo = set()
    seen = set()
    top_containers = set()
    todo.add('shiny gold')
    while len(todo):
        from_bag = todo.pop()
        if from_bag in seen:
            continue
        seen.add(from_bag)
        for container_bag in container_bags[from_bag]:
            todo.add(container_bag)

    seen.remove('shiny gold')
    top_shiny_gold = seen.intersection(bags_to_sub_bags.keys())
    return len(top_shiny_gold)

def part_2(bags_to_sub_bags):
    todo = list()
    todo.append((1, 'shiny gold'))
    total = 0
    while len(todo):
        count, from_bag = todo.pop()
        total += count
        if from_bag in bags_to_sub_bags:
            for sub_count, sub_bag in bags_to_sub_bags[from_bag]:
                todo.append(((count * sub_count), sub_bag))

    total -= 1
    return total

if __name__ == '__main__':
    print(part_1(input()))
    print(part_2(input()))
