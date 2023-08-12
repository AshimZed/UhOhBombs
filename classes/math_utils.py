import math


# Define function to calculate distance
def calc_distance(pos_1, pos_2):
  before_square = ((pos_2[0] - pos_1[0]) ** 2) + ((pos_2[1] - pos_1[1]) ** 2)
  return math.sqrt(before_square)