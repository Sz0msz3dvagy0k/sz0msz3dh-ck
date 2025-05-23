def dice_range_expression(min_val, max_val):
  dice_types = [2, 3, 4, 6, 8, 10, 20]
  needed_range = max_val - min_val

  for d in dice_types:
    if needed_range <= d - 1:
      offset = min_val - 1  
      if offset > 0:
        return f"1d{d}+{offset}"
      elif offset < 0:
        return f"1d{d}{offset}"
      else:
        return f"1d{d}"

  for d1 in dice_types:
    for d2 in dice_types:
      range_sum = (d1 - 1) + (d2 - 1)
      if needed_range <= range_sum:
        offset = min_val - 2
        parts = [f"1d{d1}", f"1d{d2}"]
        expr = "+".join(parts)
        if offset > 0: return f"{expr}+{offset}"
        elif offset < 0: return f"{expr}{offset}"
        return expr

  return "No solution"

if __name__ == '__main__':
  f = open("./input.txt", "r")
  
  for i in f:
    a = i.split(" ")
    print(dice_range_expression(int(a[0]), int(a[1])))

  f.close()