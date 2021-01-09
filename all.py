import time
import math

def do(day: int):
    print(f'day_{day:>02}')
    exec(f'from day_{day:>02} import day_{day:>02}')
    print(f'-------------')

def timing(days=range(1, 26)):
    "Report on timing of for all days."
    timings = []
    for day in days:
        t0 = time.time()
        do(day)
        t = time.time() - t0
        timings.append(t)

    print('    Day  Secs.')
    print('    ===  =====')    
    for i, t in enumerate(timings):
        day = i + 1
        stars = '*' * int(3 + math.log(t, 10))
        print(f'{stars:>4} {day:2} {t:6.3f}')

timing()