class Config:
    def __init__(self):
        # Card and game configuration
        self.suit_count = 4
        self.rank_count = 13
        self.card_count = self.suit_count * self.rank_count
        self.suits = ['H', 'D', 'C', 'S']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        # Game rules and parameters
        self.players_count = 2
        self.streets_count = 4
        self.board_card_count = [0, 3, 4, 5]
        self.hand_card_count = 2
        self.hand_count = 1326 # 52*51/2
        self.small_blind = 10
        self.big_blind = 20
        self.price_pool = 1000
        self.number_of_max_raises = 2

config = Config()
