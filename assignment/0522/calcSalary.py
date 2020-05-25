payRateDic = {
  1: 14.60,
  2: 15.60,
  3: 16.60,
  4: 17.60,
  5: 18.60,
  6: 19.60,
  7: 20.60,
  8: 21.60,
  9: 22.60,
  10: 23.60,
}

selectedPayRate = int(input("Select your payment rate: \n[1: $14.60 / 2: $15.60 / 3: $16.60 / 4: $17.60 / 5: $18.60 / 6: $19.60 / 7: $20.60 / 8: $21.60 / 9: $22.60 /10: $23.60]\n"))

if selectedPayRate not in range(11):
  print("Please select 1 ~ 10")
  exit(1)

workingHour= int(input("How much is your working hour?: "))
name = input("What is your name?: ")
payRate = payRateDic[selectedPayRate]

extraHour = 0
if workingHour > 80:
  extraHour = workingHour - 80
  workingHour = 80

gross = payRate * workingHour + payRate * 1.5 * extraHour
cpp = gross * 0.0525
ei = gross * 0.0158


res = f"""
Salary Detail

Name : {name}
Gross: {format(gross, '.2f')}
Net  : {format(gross - cpp - ei, '.2f')}
CPP  : {format(cpp, '.2f')}
EI   : {format(ei, '.2f')}
"""

print(res)