"""

This should handle many of the more complex calculations associated with poker, whether these involve collections
of cards or probability distributions over hole cards. 

It can classify poker hands into one of the 10 standard categories (straight, flush, full house, etc.) and further label them
such that any two poker hands can be compared and ranked. It can also generate utility matrices for any collection of
3, 4 or 5 public cards.

"""


class Oracle:
    NotImplementedError

    def __init__(self):
        pass

    def classify_hand(self, cards: []) -> [str]:
        """
        Classify hand and return a
        :param cards: takes a list of cards ( eg ["2H", "3C", "KS", ...])
        :return: Category and label
        """

        # Parse each card to extract its rank (2, 3, …, 10, J, Q, K, A) and suit (H, C, S, D)
        # Implement logic to identify the hand category (e.g., straight, flush, full house) based on the combination of ranks and suits.
        # Return the category and any additional labels (e.g., high card value, pairs, etc.).
        pass


    def utility_matrices(self, hand):
        """
        Utility matrices represent the strength of a hand given a set of public information (i.e. community cards)
        The utility matrices helps us make informed decisions during the game.

        :param hands:
        :param public information
        :return:
        """

    def draw(self, hand):
        """
        If there is a draw, we determen the strength of the hand and return who has the best hand
        :param hand:
        :return:
        """
        pass



    """
    def classify_poker_hand(cards):
        # Your code here to classify the hand
        # Return the category (e.g., "Straight Flush") and any additional labels
        
        # Example usage:
        hand = ["2H", "3H", "4H", "5H", "6H"]  # Straight Flush
        category, labels = classify_poker_hand(hand)
        print(f"Hand: {hand} | Category: {category} | Labels: {labels}")
    """