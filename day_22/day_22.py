
input_data = list(filter(None, open('day_22/input.txt').read().split('\n\n')))

def parse_deck(deck: str):
    deck = list(filter(None, deck.split('\n')))[1:]
    return list(map(int, deck))

def parse_decks(input_data):
    return list(map(parse_deck, input_data))

def score(deck: list):
    return sum([c * (len(deck) - i) for i, c in enumerate(deck)])

def play_game(decks: list):
    while all(map(len, decks)):
        takens = [d.pop(0) for d in decks]
        winner = takens.index(max(takens))
        takens.sort(reverse=True)
        decks[winner].extend(takens)
    return [score(d) for d in decks]

decks = parse_decks(input_data)
scores = play_game(decks)
print(str(max(scores)))

def play_game_2(decks: list):
    seens = [set() for d in decks]
    while all(map(len, decks)):

        for d, s in zip(decks, seens):
            dt = tuple(d)
            if dt in s:
                return 0
            s.add(dt)

        takens = [d.pop(0) for d in decks]

        if all([len(d) >= v for d, v in zip(decks, takens)]):
            copies = [d[:v] for d, v in zip(decks, takens)]
            winner = play_game_2(copies)
        else:
            winner = takens.index(max(takens))
        if winner != 0:
            takens = [takens[1], takens[0]]
        decks[winner].extend(takens)
    scores = list(map(lambda d: len(d) > 0, decks))
    return scores.index(True)

decks = parse_decks(input_data)
winner = play_game_2(decks)
print(str(score(decks[winner])))
