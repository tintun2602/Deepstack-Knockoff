class Config: 
    def __init__(self):
        # the number of players in the game
        self.players_count = 2
        # the number of betting rounds in the game
        self.streets_count = 4
        # the number of card suits in the deck
        self.suit_count = 4
        # the number of card ranks in the deck
        self.rank_count = 13
        # the total number of cards in the deck
        self.card_count = self.suit_count * self.rank_count
        # the number of public cards dealt in the game (revealed after the first betting round)
        self.board_card_count = [0, 3, 4, 5]
        self.hand_card_count = 2
        self.hand_count = 1326 # 52*51/2
        self.small_blind = 10
        self.big_blind = 20
        self.price_pool = 1000
        self.number_of_max_raises = 2 

config = Config()