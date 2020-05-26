def fact(number):
  if number == 0:
    return 1

  if number == 1 or number == -1:
    return number
  
  if number > 0:
    nextNum = number - 1
  else:
    nextNum = number + 1

  return number * fact(nextNum)

number = int(input("Enter a number for calculate factorial: "))

print(f"{number}! = ", fact(number))
