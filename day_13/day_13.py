input_data = list(filter(None, open('day_13/input.txt').read().split('\n')))

timestamp = int(input_data[0])
buses = list(map(lambda s: 0 if 'x' == s else int(s), input_data[1].split(',')))
buses_wait_times = list(map(lambda b: b - timestamp % b if b else 1000000, buses))
bus_and_times = list(zip(buses_wait_times, buses))
bus_and_times.sort()
print(str(bus_and_times[0][0] * bus_and_times[0][1]))

bus_arrival_deltas = list(range(0,len(buses)))
bus_and_deltas = list(filter(lambda bd: bd[0], zip(buses, bus_arrival_deltas)))

print(bus_and_deltas)

def first_mod_by_step(base, mod, delta, start, step):
    x = start
    for _ in range(0, max(base, mod)):
        x += step
        if (base * x + delta) % mod == 0:
            return x
    raise "bad"

step = 1
start = 0
base = bus_and_deltas[0][0]
for mod, delta in bus_and_deltas[1:]:
    new_start = first_mod_by_step(base, mod, delta, start, step)
    if new_start != start:
        start = new_start
        step *= mod

print(start * base)
