import random
import itertools

def get_shuffled_cards():
    kind = ("ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king")
    suites = ("hearts", "clubs", "spades", "diamonds")
    all_cards = list(itertools.product(kind, suites))
    random.shuffle(all_cards)
    return all_cards
