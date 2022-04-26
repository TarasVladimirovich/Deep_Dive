from itertools import count, cycle, repeat, islice
from collections import namedtuple

g = count(10)
print(list(islice(g, 10)))
g = count(1, 0.5)

print(list(islice(g, 10)))

g = cycle(('red', 'green', 'blue'))
print(list(islice(g, 10)))


def color():
    yield 'red'
    yield 'green'
    yield 'blue'


cols = color()
print(list(islice(cycle(cols), 11)))
Card = namedtuple('Card', 'rank suit')


def card_deck():
    ranks = tuple(str(num) for num in range(2, 11)) + tuple('JQKA')
    suits = ('Sppeds', 'Heart', 'Diamonds', 'Clubs')
    for suit in suits:
        for rank in ranks:
            yield Card(rank, suit)


hands = [list() for _ in range(4)]
index = 0
for card in card_deck():
    index = index % 4
    hands[index].append(card)
    index += 1
print(hands[0])
print(hands[1])

hands = [list() for _ in range(4)]
index = cycle((0, 1, 2, 3))
for card in card_deck():
    hands[next(index)].append(card)
print(hands[0])
print(hands[1])

hands = [list() for _ in range(4)]
hand_cycle = cycle(hands)
for card in card_deck():
    next(hand_cycle).append(card)
print(hands[0])
print(hands[1])
# Repeat
