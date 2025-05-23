def fibonacci(n):
  if not isinstance(n, int) or n < 0:
    return "N/A"
  
  fib_sequence = []
  a, b = 0, 1
  while a <= n:
    if a % 3 == 0:
      fib_sequence.append(a)
    a, b = b, a + b
  
  return ", ".join(map(str, fib_sequence)) if fib_sequence else "N/A"


with open('./input.txt', 'r') as f:
  inputs = f.read().splitlines()

for line in inputs:
  try:
    n = int(line)
    print(fibonacci(n))
  except ValueError:
    print("N/A")
