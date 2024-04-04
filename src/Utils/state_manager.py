"""
The poker state manager is primarily for generating game-state objects, primarily for use by the resolver. This is a relatively
simple object that can package up game situations from the game manager into state objects, which the resolver
can then use as in the root of a subtree. When queried with a hypothetical game state from the resolver, it can
generate some or all legal child states, thus aiding the resolver in building subtrees.

the state manager needs to know the specific rules of play so as to generate all and only the
legal successor states to any given game state.
"""

class PokerStateManager:
    def __init__(self, game_manager):
        self.game_manager = game_manager

    def generate_successor_states(self, current_state):
        legal_moves = self.generate_legal_moves(current_state)
        successor_states = []
        for move in legal_moves:
            # Create a copy of the current state
            new_state = current_state.copy()
            # Apply the move to the new state
            self.apply_move(new_state, move)
            # Add the new state to the list of successor states
            successor_states.append(new_state)
        return successor_states
    

    def apply_move(self, state, move):
        # This method applies a move to a state and updates the state accordingly
        # The implementation will depend on the specific rules of the game
        pass

    def generete_legal_child_states(self):
        """
        When queried with a hypothetical game state from the resolver, it can generate some or all legal child states.
        :return:
        """
        pass