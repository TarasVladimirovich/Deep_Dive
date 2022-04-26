from collections import namedtuple

SUITS = ('Spaders', 'Hearts', 'Diamonds', 'Clubs')
RANKS = tuple(range(2, 11)) + tuple('JQKA')

Card = namedtuple('Card', 'rank suit')


def card_gen():
    for i in range(len(SUITS) * len(RANKS)):
        suit = SUITS[i // len(RANKS)]
        rank = RANKS[i % len(RANKS)]
        yield Card(rank, suit)


def card_gen2():
    for suit in SUITS:
        for rank in RANKS:
            yield Card(rank, suit)


class CardDeck:

    SUITS = ('Spaders', 'Hearts', 'Diamonds', 'Clubs')
    RANKS = tuple(range(2, 11)) + tuple('JQKA')

    def __iter__(self):
        return CardDeck.card_gen()

    def __reversed__(self):
        return CardDeck.reversed_card_gen()

    @staticmethod
    def reversed_card_gen():
        for suit in reversed(CardDeck.SUITS):
            for rank in reversed(CardDeck.RANKS):
                yield Card(rank, suit)

    @staticmethod
    def card_gen():
        for suit in CardDeck.SUITS:
            for rank in CardDeck.RANKS:
                yield Card(rank, suit)


deck = CardDeck()
print(list(deck))
print(list(reversed(deck)))