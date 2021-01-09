def input():
    input_data = list(filter(None, open('day_19/input.txt').read().split('\n\n')))
    rules = list(filter(None, input_data[0].split('\n')))
    messages = list(filter(None, input_data[1].split('\n')))

    rules = {
        k : v for k, v in zip(
            map(lambda r: int(r.split(':')[0].strip()), rules),
            map(lambda r: list(map(lambda alt: list(map(lambda sub: sub.strip('"') if sub[0] == '"' else int(sub), alt.split())) , r.split(':')[1].strip().split('|'))), rules),
        )    
    }

    return rules, messages

def convert_rule_to_regex(rule_index, rules):
    alt_regex = []
    for alt in rules[rule_index]:
        sub_regex = []
        for sub_rule in alt:
            if type(sub_rule) is str:
                sub_regex.append(sub_rule)
            else:
                sub_regex.append(convert_rule_to_regex(sub_rule, rules))
        alt_regex.append(''.join(sub_regex))
    if len(alt_regex) == 1:
        return alt_regex[0]
    else:
        return '((' + ')|('.join(alt_regex) + '))'

import re

def part_1(input_data):
    rules, messages = input_data
    rule_0_re = convert_rule_to_regex(0, rules)
    rule_0_re = re.compile(rule_0_re)
    filtered_messages = list(filter(None, map(lambda msg: rule_0_re.fullmatch(msg), messages)))
    return len(filtered_messages)

def count_matches(msg, start, rule_re):
    count = 0
    while True:
        match = rule_re.match(msg, start)
        if not match:
            return count, start
        count += 1
        start = match.end() 
    
rule_42_re = None
rule_31_re = None

def multi_match(msg):
    start = 0
    count_42, start = count_matches(msg, start, rule_42_re)
    if count_42 < 2:
        return False
    count_31, start = count_matches(msg, start, rule_31_re)
    if count_31 < 1:
        return False
    if start != len(msg):
        return False
    return count_31 < count_42
    
def part_2(input_data):
    rules, messages = input_data

    global rule_31_re, rule_42_re
    rule_42_re = convert_rule_to_regex(42, rules)
    rule_42_re = re.compile(rule_42_re)
    rule_31_re = convert_rule_to_regex(31, rules)
    rule_31_re = re.compile(rule_31_re)

    filtered_messages = list(filter(None, map(multi_match, messages)))
    return len(filtered_messages)

if __name__ == '__main__':
    print(part_1(input()))
    print(part_2(input()))
