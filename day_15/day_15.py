def input():
    return [1,12,0,20,8,16]
    #return [0,3,6]

def play_until(spoken_when, spoken_before, just_spoken, current_turn, until_turn):
    for current_turn in range(current_turn, until_turn):
        if just_spoken in spoken_before:
            just_spoken = spoken_when[just_spoken] - spoken_before[just_spoken]
        else:
            just_spoken = 0

        #print(age)

        if just_spoken in spoken_when:
            spoken_before[just_spoken] = spoken_when[just_spoken]
            spoken_when[just_spoken] = current_turn
        else:
            spoken_before[just_spoken] = current_turn
            spoken_when[just_spoken] = current_turn

    return just_spoken

def part_1(input_data):
    spoken_when = { k:v for v,k in enumerate(input_data) }
    return play_until(spoken_when, {}, input_data[-1], len(input_data), 2020)

def part_2(input_data):
    spoken_when = { k:v for v,k in enumerate(input_data) }
    return play_until(spoken_when, {}, input_data[-1], len(input_data), 30000000)

if __name__ == '__main__':
    print(part_1(input()))
    print(part_2(input()))
