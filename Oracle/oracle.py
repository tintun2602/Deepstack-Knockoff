"""

This should handle many of the more complex calculations associated with poker, whether these involve collections
of cards or probability distributions over hole cards. 

It can classify poker hands into one of the 10 standard categories (straight, flush, full house, etc.) and further label them
such that any two poker hands can be compared and ranked. It can also generate utility matrices for any collection of
3, 4 or 5 public cards.

"""

class Oracle: 
    NotImplementedError