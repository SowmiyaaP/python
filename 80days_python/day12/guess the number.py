from random import randint
import random

print("WELCOME TO THE GUESSING GAME")
print("THINKING BETWEEN 1 TO 100")

def makeaguess(chance,num,attempt):
    
    if chance == num:
          print("you have guessed it right!!")
    elif chance > num:
          print("too high")
          return attempt-1
    elif chance < num:
          print("too low")
          return attempt - 1

def levels():
  level=input("Pick a level 'easy' or 'hard':")
  if level=="easy":
      return 10
  else:
      return 5


num = random.randint(1,100)
attempt = levels()
chance = 0
while chance!= num:
  print(f"You have {attempt} attempts remaining to guess the number.")
  chance = int(input("make a guess:"))
  attempt= makeaguess(chance, num, attempt)
  if attempt == 0:
      print("You've run out of guesses, you lose.")
      break
  elif chance != num:
      print("Guess again.")


