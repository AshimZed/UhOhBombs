import random

from .math_utils import calc_distance

# Create player character
class Player:
  moves = {'w': (0, 1), 'a': (-1, 0), 's': (0, -1), 'd': (1, 0),}

  def __init__(self, player_pos = None):
    if player_pos is None:
      player_pos = [0, 0]
    self.player_pos = player_pos

  # Define function to handle player moves
  def handle_move(self, move, map):
    if move in self.moves:
      self.player_pos[0] += self.moves[move][0]
      self.player_pos[1] += self.moves[move][1]
    elif move == 'help':
      print('Moves: Right = A, Left = D, Up = W, Down = S Check Position = check')
    elif move == 'check':
      print(self.player_pos)
    elif move == 'bombs':
      print(map.bombs)
    else:
      print('Invalid Command: Type help')
    return map.boundary > self.player_pos[0] > -map.boundary and map.boundary > self.player_pos[1] > -map.boundary

  # Define function to compute radiation level at current position
  def calc_rad_level(self, bombs):
    rad_level = 0
    for i in bombs:
      rad_level += 1 / (calc_distance(self.player_pos, i)**2)
    rad_level *= 1 + random.uniform(-0.1, 0.1)
    return rad_level

  # Define function to check radiation sensor
  def check_sensor(self, bombs):
    raw_rad_level = self.calc_rad_level(bombs)
    percent_rad_level = raw_rad_level * 100
    return round(percent_rad_level, 2)
  
  # Define function to flag suspected bomb locations
  # def flag(self,map):
  #   flag_input = input('Flag: ').lower()
    