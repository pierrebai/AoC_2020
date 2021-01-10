import time
import math
import importlib

def do(day: int):
    mod = importlib.import_module(f'day_{day:>02}.day_{day:>02}')
    input_data = mod.input()
    res1 = mod.part_1(input_data)
    input_data = mod.input()
    res2 = mod.part_2(input_data)
    return res1, res2

def timing(days=range(1, 26)):
    "Report on timing of for all days."
    print('    Day  Secs.  Answers')
    print('    ===  =====  =======')    
    for day in days:
        t0 = time.time()
        answers = do(day)
        t = time.time() - t0
        if answers != [None, None]:
            stars = '*' * int(3 + math.log(t, 10))
            print(f'{stars:>4} {day:2} {t:6.3f}  {answers}')

timing()