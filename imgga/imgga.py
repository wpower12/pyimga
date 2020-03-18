import math
import random

MULT_SCALE = 1.0
SIN_SCALE = 1.5
COS_SCALE = 1.5

# Atomic elements of the procedure function
# [KIND, NUM_PARAMETERS]
ATOMS = [["A", 2],  # Add
         ["D", 2],  # Difference
         ["M", 2],  # Multiplication
         ["S", 1],  # Sin
         ["C", 1],  # Cos
         ["N", 1],  # Negate
         ["X", 1],
         ["Y", 1]]
TERMINALS = ["X", "Y"]  # Inputs are the terminals

class node:

    def __init__(self, kind):
        self.kind = kind
        self.children = []

    def eval(self, X, Y):
        # First we check if this node is a terminal (only have the two)
        if self.kind == "X":
            return X
        if self.kind == "Y":
            return Y

        # If not a terminal, then we collect the parameters be eval'ing the children. need to be careful
        # because some kinds of nodes only have 1 child/parameter.
        p1 = self.children[0].eval(X, Y)
        if len(self.children) == 2:
            p2 = self.children[0].eval(X, Y)

        # -- Double Parameter
        # Add
        if self.kind == "A":
            return p1 + p2
        # Difference
        if self.kind == "D":
            return p1 - p2
        # Scaled Mult
        if self.kind == "M":
            return p1 * p2 * MULT_SCALE

        # -- Single Parameter
        # Sin
        if self.kind == "S":
            return math.sin(p1) * SIN_SCALE
        # Cos
        if self.kind == "C":
            return math.cos(p1) * COS_SCALE

        # Negate
        if self.kind == "N":
            return -1.0 * p1


def make_individual(remaining_depth):
    if remaining_depth == 0:
        kind = random.choice(TERMINALS)
        return node(kind)
    else:
        kind, num_params = random.choice(ATOMS)

        if kind in TERMINALS:
            return node(kind)
        else:
            n = node(kind)
            for i in range(num_params):
                n.children.append(make_individual(remaining_depth - 1))
            return n
