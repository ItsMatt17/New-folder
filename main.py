import random

def greaterOrLower(num1, num2):
  if num1 > num2:
    print("The number is smaller")
  else:
    print("The number is larger")

randomNum = random.randint(1, 10)

def game():
  while True:
    guess = int(input("Please give your guess: "))
    if guess == randomNum:
        print("correct!")
        break
    else:
      greaterOrLower(guess, randomNum)
      continue

game()

while True:
  nextResponse = input("Would you like to continue playing? y/n: ")
  responsesContinue = ["yes", "y"]
  if nextResponse == responsesContinue[0] or nextResponse == responsesContinue[1]:
    game()
  else:
    print("goodbye")
    quit()


