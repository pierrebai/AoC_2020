import re
from collections import defaultdict

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

input_data = list(filter(None, open('day_07/input.txt').read().split('\n')))
top_bags = list(map(extract_top_bag, map(lambda x: '1 ' + x, input_data)))
sub_bags = list(map(extract_sub_bags, input_data))
bags_to_sub_bags = {
    k[1]:v for k, v in zip(top_bags, sub_bags)
}

top_bags = set(map(lambda x: x[1], top_bags))

bags_to_containers = defaultdict(set)
for parent_bag, sub_bags in bags_to_sub_bags.items():
    if sub_bags:
        for count, sub_bag in sub_bags:
            bags_to_containers[sub_bag].add(parent_bag)

todo = set()
seen = set()
top_containers = set()
todo.add('shiny gold')
while len(todo):
    from_bag = todo.pop()
    if from_bag in seen:
        continue
    seen.add(from_bag)
    for container_bag in bags_to_containers[from_bag]:
        todo.add(container_bag)

seen.remove('shiny gold')
top_shiny_gold = seen.intersection(top_bags)
print(len(top_shiny_gold))

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
print(str(total))