#
# www.youtube.com/@mersthub_mentors
#


def reveal_deck(deck: list):
    N = len(deck)
    deck.sort()
    idx = [i for i, _ in enumerate(deck)]
    output = [0] * N;
    pick = True
    i = 0
    while idx:
        if pick:
            output[idx.pop(0)] = deck[i]
            i += 1
            pick = False
        else:
            idx.append(idx.pop(0))
            pick = True

    return output


Cards = [17, 13, 11, 22, 3, 5, 9, 8]
res = reveal_deck(Cards)
print(res)
