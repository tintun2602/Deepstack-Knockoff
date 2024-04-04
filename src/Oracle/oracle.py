from collections import Counter
from typing import Tuple
from Settings.config import Config

config = Config()

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}{self.suit}"


class Deck:
    def __init__(self):
        self.config = config # Use the Config instance in Deck

    def generate_deck(self):
        return [Card(rank, suit) for rank in self.config.ranks for suit in self.config.suits]

class Oracle:
    def __init__(self):
        self.config = config

    
    def classify_hand(self, cards: list[Card]) -> Tuple[str, str]:
        # Count the occurrences of each rank and suit
        rank_counts = Counter(card.rank for card in cards if card.rank in self.config.ranks)
        suit_counts = Counter(card.suit for card in cards if card.suit in self.config.suits)
        
        # Check for a Royal Flush
        if len(suit_counts) == 1 and rank_counts == Counter({'A': 1, 'K': 1, 'Q': 1, 'J': 1, '10': 1}):
            return "Royal Flush", ""
        
        # Check for a Straight Flush
        if len(suit_counts) == 1 and self.is_straight(rank_counts):
            return "Straight Flush", ""
        
        # Check for a Four of a Kind
        if 4 in rank_counts.values():
            return "Four of a Kind", ""
        
        # Check for a Full House
        if len(rank_counts) == 2 and list(rank_counts.values()) in ([2, 3], [3, 2]):
            return "Full House", ""
        
        # Check for a Flush
        if len(suit_counts) == 1:
            return "Flush", ""
        
        # Check for a Straight
        if self.is_straight(rank_counts):
            return "Straight", ""
        
        # Check for Three of a Kind
        if 3 in rank_counts.values():
            return "Three of a Kind", ""
        
        # Check for Two Pair
        if len(rank_counts) == 3 and 2 in rank_counts.values():
            return "Two Pair", ""
        
        # Check for a Pair
        if 2 in rank_counts.values():
            return "Pair", ""
        
        # Default to High Card
        return "High Card", ""

    def is_straight(self, rank_counts):
        # Check if the ranks form a straight
        ranks = sorted(rank_counts.keys(), key=lambda r: ('A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2').index(r))
        return ranks == list(range(min(ranks), max(ranks)+1))

 
    def utility_matrices(self, hand):
       """
        Utility matrices represent the strength of a hand given a set of public information (i.e. community cards)
        The utility matrices helps us make informed decisions during the game.

        :param hands:
        :param public information
        :return: """
       
    
    def draw(self, hand):
        """ 
        If there is a draw, we determen the strength of the hand and return who has the best hand
        :param hand:
        :return:
        """
        return "Placeholder draw evaluation"


