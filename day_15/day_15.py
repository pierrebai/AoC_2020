input_data = [1,12,0,20,8,16]
#input_data = [0,3,6]

def play_until(spoken_when, just_spoken, current_turn, until_turn):
    while current_turn < until_turn:
        if len(spoken_when[just_spoken]) > 1:
            age = spoken_when[just_spoken][-1] - spoken_when[just_spoken][-2]
        else:
            age = 0

        #print(age)

        if age in spoken_when:
            spoken_when[age] = [spoken_when[age][-1], current_turn]
        else:
            spoken_when[age] = [current_turn]

        just_spoken = age
        current_turn += 1

    return just_spoken

spoken_when = { k:[v] for v,k in enumerate(input_data) }
print(str(play_until(spoken_when, input_data[-1], len(input_data), 2020)))

spoken_when = { k:[v] for v,k in enumerate(input_data) }
print(str(play_until(spoken_when, input_data[-1], len(input_data), 30000000)))
