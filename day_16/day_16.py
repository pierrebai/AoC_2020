fields = None

def input():
    global fields
    input_data = list(filter(None, open('day_16/input.txt').read().split('\n\n')))
    fields = list(filter(None, input_data[0].split('\n')))
    fields = list(map(parse_field, fields))
    your_ticket = parse_ticket(input_data[1].split('\n')[1])
    nearby_tickets = list(map(parse_ticket, list(filter(None, input_data[2].split('\n')))[1:]))
    return fields, your_ticket, nearby_tickets

def parse_ticket(ticket):
    fields = filter(None, ticket.split(','))
    return list(map(int, fields))

def parse_field(field):
    name, ranges = field.split(':')
    ranges = ranges.split(' or ')
    ranges = list(map(lambda r: r.split('-'), ranges))
    ranges = list(map(lambda r: (int(r[0].strip()), int(r[1].strip())), ranges))
    return name, ranges

def valid_for_ranges(field, ranges):
    for r in ranges:
        if r[0] <= field <= r[1]:
            return True
    return False
    
def valid_field(field):
    for name, ranges in fields:
        if valid_for_ranges(field, ranges):
            return True
    return False

def extract_invalid_fields(ticket):
    invalids = []
    for field in ticket:
        if not valid_field(field):
            invalids.append(field)
    return invalids

def sum_invalid_fields(ticket):
    return sum(extract_invalid_fields(ticket))

def part_1(input_data):
    nearby_tickets = input_data[2]
    return sum(map(sum_invalid_fields, nearby_tickets))

def valid_ticket(ticket):
    return all(map(valid_field, ticket))

def nonify_invalid_ticket(ticket):
    return ticket if valid_ticket(ticket) else None

def valid_for_all_tickets(ranges, index, tickets):
    for ticket in tickets:
        if not valid_for_ranges(ticket[index], ranges):
            return False
    return True

def part_2(input_data):
    fields, your_ticket, nearby_tickets = input_data
    valid_nearby_tickets = list(filter(None, map(nonify_invalid_ticket, nearby_tickets)))
    posible_field_ids = {}
    for name, ranges in fields:
        possible_indices = set()
        for ticket_field_index in range(0, len(your_ticket)):
            if valid_for_all_tickets(ranges, ticket_field_index, valid_nearby_tickets):
                possible_indices.add(ticket_field_index)
        posible_field_ids[name] = possible_indices

    field_ids = {}
    while True:
        taken_ids = set()
        for name, possible_indices in posible_field_ids.items():
            if len(possible_indices) == 1:
                id = possible_indices.pop()
                field_ids[name] = id
                taken_ids.add(id)
        if not taken_ids:
            break
        for id in taken_ids:
            for name, possible_indices in posible_field_ids.items():
                if id in possible_indices:
                    possible_indices.remove(id)

    total = 1
    for name, id in field_ids.items():
        if name.startswith('departure'):
            total *= your_ticket[id]

    return total

if __name__ == '__main__':
    print(part_1(input()))
    print(part_2(input()))
