locations = {0:"You are sitting in front of the computer",
             1:"You are standing in front of the road before a brick building",
             2:"You are at the top of a hill",
             3:"You are inside a buiding",
             4:"You are in a valler besides a stream",
             5:"You are in the forest"}

exits = {0: {"Q":0},
         1: {"W":2, "E":3, "N":5, "S":4, "Q":0},
         2: {"N":5, "Q":0},
         3: {"W":1, "Q":0},
         4: {"N":1, "W":2, "Q":0},
         5: {"W":2, "S":1,"Q":0}}

# Solution(Copied)
loc = 1
forest = list(locations[xit] for xit in exits if loc in exits[xit].values())
print(forest)