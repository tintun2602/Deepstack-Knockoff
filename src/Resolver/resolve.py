"""
Resolving begins with the production of a subtree, which might be produced in its entirety but may also be built
incrementally, with expansions occurring during each traversal of the tree. The word rollout reflects both a) the
possibility of incremental subtree expansion, and b) the possibility that the resolver may only explore some (not all)
children of certain nodes.
"""

class Resolver:
    NotImplementedError 