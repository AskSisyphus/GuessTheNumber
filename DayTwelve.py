import random
from replit import clear
difficulty = input("Guess the correct number in my head!\nType 'easy' for easy mode and 'hard' for hard mode: ")

if difficulty == "easy":
  lives = 10
elif difficulty == "hard":
  lives = 5
else:
  print("Invalid choice. Goodbye.")

print(f"You have {lives} lives to start out with.")

number = random.randint(1,100)
#print(number)
first_guess = int(input("The number in my head is between 1 and 100. Make your guess: "))

if first_guess > number:
  print("Too high. ")
  remaining_lives = lives - 1
elif first_guess < number:
  print("Too low. ")
  remaining_lives = lives - 1
elif first_guess == number:
  remaining_lives = lives -1
  print("You got it right on the first try! Great job! ")
  quit()

end_of_game = True
while not end_of_game in range(1):
  following_guesses = int(input(f"You now have {remaining_lives} lives. Guess again: "))
  if following_guesses > number:
    print("Too high. ")
    remaining_lives = remaining_lives -1
    if remaining_lives == 0:
      print("You have no more lives left. You lose!")
      end_of_game = True
      break
      clear()
  elif following_guesses < number:
    print("Too low. ")
    remaining_lives = remaining_lives -1
    if remaining_lives == 0:
      print("You have no more lives left. You lose!")
      end_of_game = True
      break
      clear()
  elif following_guesses == number:
    end_of_game = True
    print("Correct! You win! ")
    break
