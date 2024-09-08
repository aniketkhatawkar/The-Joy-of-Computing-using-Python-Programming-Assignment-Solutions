ladders = input().split(' ')
ladders = [int(num) for num in ladders]
snakes = input().split(' ')
snakes = [int(num) for num in snakes]
current_position = int(input())
die_roll = int(input())
def move_player(ladders, snakes, current_position, die_roll):
  new_position = current_position + die_roll
  if new_position in ladders:
    return 1
  elif new_position in snakes:
    return -1
  else:
    return 0
print(move_player(ladders, snakes, current_position, die_roll) , end='')