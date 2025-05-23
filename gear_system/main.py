import ast
from collections import deque
left_lever = [1, 1, 0]
right_lever = [0, 1, 1]

gears = [3, 3, 3]

def rotate(lever, gears):
  new_gears = gears[:]
  for index in range(len(gears)):
    new_gears[index] += lever[index]
    if new_gears[index] > 3:
      new_gears[index] -= 3
  return new_gears

def find_solution(target, max_moves=8):

  initial_state = (gears, [])
  queue = deque([initial_state])
  visited = set()

  while queue:
    current_gears, moves = queue.popleft()

    if current_gears == target:
      return " ".join(moves)

    state_tuple = tuple(current_gears)
    if state_tuple in visited:
      continue
    visited.add(state_tuple)

    if len(moves) >= max_moves:
      continue

    queue.append((rotate(left_lever, current_gears), moves + ["left"]))
    queue.append((rotate(right_lever, current_gears), moves + ["right"]))

  return "Megoldhatatlan"



if __name__ == '__main__':
  f = open("./input.txt", "r")

  for line in f:
        parts = line.strip().split(']', 1)
        lst = ast.literal_eval(parts[0] + ']')
        number = int(parts[1].strip()) if len(parts) > 1 and parts[1].strip() else 8
        print(find_solution(lst, number))

  f.close()