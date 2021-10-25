import shuffled
import random


class Deck:
    def __init__(self):
        self.available = shuffled.get_shuffled_cards()
        self.spent = []

    def shuffle(self):
        random.shuffle(self.available)
        return self

    def get_cards(self, count=1):
        random_pick = random.choices(self.available, count)
        return random_pick


kartis = Deck()
print(kartis.shuffle())
