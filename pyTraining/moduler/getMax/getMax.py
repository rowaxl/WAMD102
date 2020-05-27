def fromList(numbers: [int]) -> int:
  maxValue = numbers[0]
  for number in numbers:
    if number > maxValue:
      maxValue = number

  return maxValue