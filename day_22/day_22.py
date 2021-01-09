def input():
    input_data = list(filter(None, open('day_22/input.txt').read().split('\n\n')))
    return parse_decks(input_data)

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

def part_1(decks):
    scores = play_game(decks)
    return max(scores)

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
            taken = takens.pop(winner)
            takens.insert(0, taken)
        else:
            winner = takens.index(max(takens))
            takens.sort(reverse=True)
        decks[winner].extend(takens)
    scores = list(map(lambda d: len(d) > 0, decks))
    return scores.index(True)

def part_2(decks):
    winner = play_game_2(decks)
    return score(decks[winner])

if __name__ == '__main__':
    print(part_1(input()))
    print(part_2(input()))
