while True:
  value = input("Height: ")
  if (value.isnumeric()):
    height = int(value)
    if (height > 0):
      break

for i in range(height):
  for j in range(height - i - 1):
    print(" ",end="")
  for j in range(2 * i + 1):
    if j % 2 == 0:
      print("*", end="")
    else:
      print(" ", end="")
  print()
