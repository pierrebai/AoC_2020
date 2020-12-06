import re
letters = re.compile('''[a-z]''')
def str_to_letters_set(s):
    return set(filter(lambda x: letters.match(x), s))

groups = open('day_06/input.txt').read().split('\n\n')
groups_answers = map(lambda g: str_to_letters_set(g), groups)
groups_counts = map(len, groups_answers)
total_count = sum(groups_counts)
print(str(total_count))

def intersect_all(s):
    result = s[0]
    for o in s[1:]:
        # Unfortunately, internal group split produces an
        # empty set for teh last entry in the input, so
        # we must protect agaist empty sets...
        if o:
            result.intersection_update(o)
    return result

groups_persons = map(lambda g: g.split('\n'), groups)
groups_persons_answers = map(lambda g: list(map(lambda p: str_to_letters_set(p), g)), groups_persons)
groups_common_answers = map(lambda g: intersect_all(g), groups_persons_answers)
groups_common_counts = map(len, groups_common_answers)
total_common_count = sum(groups_common_counts)
print(str(total_common_count))

