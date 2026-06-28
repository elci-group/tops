import random

class Card:
    def __init__(self, name, attribute1, attribute2, attribute3):
        self.name = name
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.attribute3 = attribute3

class Deck:
    def __init__(self):
        self.cards = [
            Card('Card1', 10, 5, 8),
            Card('Card2', 8, 6, 9),
            Card('Card3', 7, 4, 6),
            Card('Card4', 9, 7, 5),
            Card('Card5', 6, 8, 7)
        ]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def draw_card(self, deck):
        self.cards.append(deck.deal_card())

    def play_card(self):
        return self.cards.pop(0)

def game_loop():
    deck = Deck()
    player1 = Player('Player1')
    player2 = Player('Player2')

    for _ in range(5):
        player1.draw_card(deck)
        player2.draw_card(deck)

    while len(player1.cards) > 0 and len(player2.cards) > 0:
        card1 = player1.play_card()
        card2 = player2.play_card()
        print(f'{player1.name} plays: {card1.name} - Attribute1: {card1.attribute1}, Attribute2: {card1.attribute2}, Attribute3: {card1.attribute3}')
        print(f'{player2.name} plays: {card2.name} - Attribute1: {card2.attribute1}, Attribute2: {card2.attribute2}, Attribute3: {card2.attribute3}')
        if card1.attribute1 > card2.attribute1:
            print(f'{player1.name} wins this round!\n')
            player1.cards.extend([card1, card2])
        elif card1.attribute1 < card2.attribute1:
            print(f'{player2.name} wins this round!\n')
            player2.cards.extend([card1, card2])
        else:
            print('It's a tie!\n')
            player1.cards.append(card1)
            player2.cards.append(card2)
    if len(player1.cards) > 0:
        print(f'{player1.name} wins the game!')
    else:
        print(f'{player2.name} wins the game!')

game_loop()