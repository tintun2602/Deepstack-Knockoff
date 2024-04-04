import random
from player import Player, AIPlayer
from Settings.config import Config


config = Config()


class PokerGameManager:
    def __init__(self):
        self.players = []
        self.dealer = None
        self.public_cards = []
        self.private_cards = {}
        self.pot = 0
        self.current_bet = 0 
        self.game_state = "pre-flop"
        self.config = config

    def add_player(self, name, chips, player_type='human'): 
        if player_type == 'human':
            player = Player(name, chips, player_type)
        elif player_type == 'AI':
            player = AIPlayer(name, chips, 0.5) # Example resolution parameter
        self.players.append(player)

    def remove_player(self, name): 
        for player in self.players: 
            if player.name == name:
                self.players.remove(player)
                break

    def deal_cards(self):
        self.public_cards = random.sample(range(1,53),5)
        for player in self.players: 
            player.hand = random.sample(range(1,53),2)

    def deal_private_cards(self): 
        for player in self.players: 
            player.hand += random.sample(range(1,53),2)

    def start_game(self): 
        if len(self.players) > 6:
            raise ValueError("Cannot start a game with more than 6 players.")
        self.deal_cards()
        self.deal_private_cards()
        self.game_state = "pre-flop"

    def determine_winner(self):
        pass

    def update_pot(self, amount): 
        self.pot += amount

    def update_bet(self, amount):
        self.current_bet += amount

    def player_action(self, player_name, action, amount):
        pass

    def rotate_dealer(self):
        if not self.dealer:
            self.dealer = self.players[0]
        else: 
            current_index = self.players.index(self.dealer)
            self.dealer = self.players[(current_index + 1) % len(self.players)]

    def next_round(self):
        pass

    def enforce_restrictions(self, stage):
        pass

    def is_game_over(self):
        pass

    def get_current_state(self):
        # This method returns the current state of the game
        # The state could be a dictionary or an object containing the game state
        state = {
            "players": self.players,
            "dealer": self.dealer, 
            "public_cards": self.public_cards, 
            "private_cards": self.private_cards,
            "pot": self.pot,
            "current_bet": self.current_bet, 
            "game_state": self.game_state
        }
        return state







            


