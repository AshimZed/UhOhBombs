from classes.player import Player
from classes.map_gen import Map

player = Player()
current_map = Map(30, player.player_pos)

while True:
  print('Radiation Readings: ' + str(player.check_sensor(current_map.bombs)) + '%')
  move = input('Move: ').lower()
  in_boundary = player.handle_move(move, current_map)
  if player.player_pos in current_map.bombs:
      print('OH NO! You exploded!')
      break
  if not in_boundary:
      print('Player reached boundary at: ' + str(player.player_pos))
      break