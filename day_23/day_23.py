from collections import deque

def input():
    return [9, 6, 1, 3, 8, 5, 2, 7]

# Circular list of cups.
class cup:
    def __init__(self, v):
        self.label = v
        self.next = self

cup_finder = dict

# Add a cup with the given label after the given cup,
# maintaining the circular list. Works even if the
# after-cup is None, to create the first cup.
# Add it to the cup finder, too.
def add_cup_after(after: cup, finder: cup_finder, label: int):
    new_cup = cup(label)
    if after:
        new_cup.next = after.next
        after.next = new_cup
    finder[label] = new_cup
    return new_cup

# Remove the three cups after the given one and return them.
# Note: the removed cups form a simple list, not a circular one.
def cut_next_three(current: cup):
    first = current.next
    last = current.next.next.next
    current.next = last.next
    last.next = None
    return first

# Reduce label by one, with wrap around if zero or less.
def decrease_label(label: int, max_cup: int):
    return max_cup if label == 1 else label - 1

# Verify if a label is in the linked list of cups.
# Note: linked list is not circular.
def is_label_in(picked: cup, label: int):
    while picked:
        if label == picked.label:
            return True
        picked = picked.next
    return False

# Insert the non-circular list of cups after the given cup
# which is in a circular list. Keep the resulting list circular.
def insert_after(after: cup, picked: cup):
    last = after.next
    after.next = picked
    while picked.next:
        picked = picked.next
    picked.next = last

# Execute a single crab game move.
def crab_move(current: cup, finder: cup_finder, max_label: int):
    picked_cups = cut_next_three(current)
    destination_label = decrease_label(current.label, max_label)
    while is_label_in(picked_cups, destination_label):
        destination_label = decrease_label(destination_label, max_label)
    destination_cup = finder[destination_label]
    insert_after(destination_cup, picked_cups)

def part_1(labels):
    finder = cup_finder()
    current = add_cup_after(None, finder, 4)
    last = current
    for label in labels:
        last = add_cup_after(last, finder, label)

    max_label = len(finder)

    for i in range(0, 100):
        crab_move(current, finder, max_label)
        current = current.next

    labels = []
    cup_to_print = finder[1].next
    for i in range(0, max_label-1):
        labels.append(str(cup_to_print.label))
        cup_to_print = cup_to_print.next
    return ''.join(labels)

def part_2(labels):
    finder = cup_finder()
    current = add_cup_after(None, finder, 4)
    last = current
    for label in labels:
        last = add_cup_after(last, finder, label)

    for label in range(10, 1000000 + 1):
        last = add_cup_after(last, finder, label)

    max_label = len(finder)

    for i in range(0, 10000000):
        crab_move(current, finder, max_label)
        current = current.next

    one_cup = finder[1]
    label_1 = one_cup.next.label
    label_2 = one_cup.next.next.label

    return label_1 * label_2

if __name__ == '__main__':
    print(part_1(input()))
    print(part_2(input()))
