from collections import deque

def decrease_label(label: int, max_cup: int):
    return max_cup if label == 1 else label - 1

def rotate_list_left(l, count):
    de = deque(l)
    de.rotate(-count)
    return list(de)

def crab_move(cups: list):
    max_cup = len(cups)
    picked = cups[1:4]
    del cups[1:4]
    destination_label = decrease_label(cups[0], max_cup)
    while destination_label in picked:
        destination_label = decrease_label(destination_label, max_cup)
    destination = cups.index(destination_label) + 1
    cups[destination:destination] = picked
    cups = rotate_list_left(cups, 1)
    return cups

cups = [3,8,9,1,2,5,4,6,7]
#cups = [4,9,6,1,3,8,5,2,7]
for i in range(0, 100):
    cups = crab_move(cups)

cups = rotate_list_left(cups, cups.index(1))
del cups[0]
print(''.join(map(str, cups)))


#cups = [4,9,6,1,3,8,5,2,7]
#cups.extend([i for i in range(10, 1000000+1)])
#for i in range(0, 10000000):
#    if i % 1000 == 0:
#        print('.')
#    cups = crab_move(cups)

#one = cups.index(1)
#print(cups[one+1] * cups[one+2])
