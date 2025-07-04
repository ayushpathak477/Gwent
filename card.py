import random

# -----------------------
# Card Class
# -----------------------
class Card:
    def __init__(self, name, strength, row, ability=None):
        self.strength = strength
        self.name = name
        self.row = row
        self.ability = ability

    def __str__(self):
        ability_str = f" ({self.ability})" if self.ability else ""
        return f"{self.name} ({self.row}) - Strength: {self.strength}{ability_str}"

# -----------------------
# Deck Class
# -----------------------
class Deck:
    def __init__(self, cards):
        self.cards = cards  # list of Card objects

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if self.cards:
            return self.cards.pop(0)  # draw from top of deck
        else:
            print("Deck is empty!")
            return None

    def __str__(self):
        return f"Deck with {len(self.cards)} cards remaining."

# -----------------------
# Player Class
# -----------------------
class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.hand = []
        self.score = 0

    def draw_hand(self, num_cards):
        for _ in range(num_cards):
            card = self.deck.draw_card()
            if card:
                self.hand.append(card)

    def play_card(self, card_index):
        if 0 <= card_index < len(self.hand):
            return self.hand.pop(card_index)
        else:
            print("Invalid card index.")
            return None

    def __str__(self):
        return f"Player {self.name} - Hand: {len(self.hand)} cards, Deck: {len(self.deck.cards)} cards, Score: {self.score}"

# -----------------------
# Test Run
# -----------------------

# Create a deck
# deck = Deck([
#     Card('Geralt of Rivia', 15, 'melee'),
#     Card('Yennefer', 7, 'ranged'),
#     Card('Triss Merigold', 7, 'ranged'),
#     Card('Clear Weather', 0, 'special', 'clear_weather')
# ])
# deck.shuffle()

# # Create a player with the deck
# player = Player("Geralt", deck)

# # Draw 2 cards into hand
# player.draw_hand(2)
# print(player)

# # Play a card from hand (index 0)
# played_card = player.play_card(0)
# print(f"{player.name} played: {played_card}")

# # Show player after playing a card
# print(player)

# -----------------------
# Board Class
# -----------------------

class Board:
    def __init__(self):
        self.rows = {
            "player" : {"melee": [], "ranged": [], "siege": []},
            "opponent": {"melee": [], "ranged": [], "siege": []}
        }

    def add_card(self, player_name, card):
        if card.row in self.rows[player_name]:
            self.rows[player_name][card.row].append(card)
        else:
            print(f"Invalid row: {card.row} for player {player_name}")
        
    def get_score(self, player_name):
        total = 0
        for row in self.rows[player_name].values():
            total += sum(card.strength for card in row)
        return total
        
    def __str__(self):
        result = ""
        for side in self.rows:
            result += f"{side.capitalize()}:\n"
            for row, cards in self.rows[side].items():
                row_str = ", ".join(str(card) for card in cards)
                result += f" {row}: {row_str}\n"
        return result
    
board = Board()
board.add_card("player", Card("Geralt of Rivia", 15, "melee"))
board.add_card("player", Card("Triss Merigold", 7, "ranged"))
board.add_card("opponent", Card("Yennefer", 7, "ranged"))

print(board)
print("Player score:", board.get_score("player"))
print("Opponent score:", board.get_score("opponent"))
