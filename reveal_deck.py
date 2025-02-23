#
# www.youtube.com/@mersthub_mentors
#

from collections import deque


class RevealDeck:
    def __init__(self, deck):
        self.deck = deck
        self.n = len(deck)
        self.deck.sort()
        self.output = [0] * len(self.deck)
        self.idx = deque(range(self.n))

    def play(self):
        pick = True
        i = 0

        while self.idx:
            if pick:
                self.output[self.idx.popleft()] = self.deck[i]
                i += 1
                pick = False
            else:
                self.idx.append(self.idx.popleft())
                pick = True

        return self.output


if __name__ == "__main__":
    cards = [7, 13, 11, 22, 33, 5, 19, 8]

    res = RevealDeck(cards).play()
    print(f"Results using deque:\n{res}")
