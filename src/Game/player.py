class Player:
    def __init__(self, name, chips, player_type): 
        self.name = name 
        self.chips = chips 
        self.hand = []
        self.in_game = True
        self.type = player_type

class AIPlayer(Player):
    def __init__(self, name, chips, resolution_parameter):
        super().__init__(name, chips, "AI")
        self.resolution_parameter = resolution_parameter
