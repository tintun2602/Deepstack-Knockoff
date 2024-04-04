"""
The poker state manager is primarily for generating game-state objects, primarily for use by the resolver. This is a relatively
simple object that can package up game situations from the game manager into state objects, which the resolver
can then use as in the root of a subtree. When queried with a hypothetical game state from the resolver, it can
generate some or all legal child states, thus aiding the resolver in building subtrees.

the state manager needs to know the specific rules of play so as to generate all and only the
legal successor states to any given game state.
"""

class StateManager:
    def __init__(self):
        pass

    def generete_legal_child_states(self):
        """
        When queried with a hypothetical game state from the resolver, it can generate some or all legal child states.
        :return:
        """
        pass