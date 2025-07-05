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
# Board Class
# -----------------------
class Board:
    def __init__(self):
        self.rows = {
            "player": {"melee": [], "ranged": [], "siege": []},
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
                row_str = ", ".join(str(card) for card in cards) or "Empty"
                result += f"  {row}: {row_str}\n"
        return result

# -----------------------
# Play Turn Function (OUTSIDE Board)
# -----------------------
def play_turn(player, board, is_player=True):
    if is_player:
        print(f"\n{player.name}'s Hand:")
        for idx, card in enumerate(player.hand):
            print(f"{idx}: {card}")
        choice = input("Choose a card to play (index) or 'p' to pass: ")
        if choice == 'p':
            print(f"{player.name} passed.")
            return False  # player passed
        try:
            card_index = int(choice)
            card = player.play_card(card_index)
            if card:
                board.add_card("player", card)
                print(f"{player.name} played: {card}")
        except (ValueError, IndexError):
            print("Invalid input. Try again.")
            return play_turn(player, board, is_player)
    else:
        # Opponent AI (random card play for now)
        if player.hand:
            card_index = random.randint(0, len(player.hand) - 1)
            card = player.play_card(card_index)
            board.add_card("opponent", card)
            print(f"{player.name} played: {card}")
        else:
            print(f"{player.name} passed.")
            return False  # opponent passed
    return True  # played a card
