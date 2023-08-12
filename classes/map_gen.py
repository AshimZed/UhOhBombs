import random

# Generate maps with size and bomb locations
class Map:

  def __init__(self, size, player_pos, flags = None):
    self.boundary = round(size / 2)
    self.player_pos = player_pos
    self.bombs = self.gen_bomb()
    if flags == None:
      flags = []

  def gen_bomb(self):
    num_bombs = random.randint(1, round(self.boundary ** 1.5))
    bombs = []
    for i in range(num_bombs):
      new_bomb = []
      while new_bomb not in bombs:
        new_bomb = [random.randint(-self.boundary + 1, self.boundary), random.randint(-self.boundary + 1, self.boundary)]
        if new_bomb != self.player_pos:
          bombs.append(new_bomb)
    return bombs