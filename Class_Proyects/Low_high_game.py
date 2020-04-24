import random

def high_low_game():
  guesses_taken = 0
  min_num = 0
  max_num = 100

  print("Welcom to 'High-low Game'. How can I call you?")
  username = input()

  number = random.randint(min_num, max_num)
  print(f"OK {username}, I'm thinking in a number between {str(min_num)} and {str(max_num)}, and you have 10 attempts")

  def guess_try():
    pass

  while True:
    while guesses_taken < 10:
      print("Are you capable to guess my number? write your guess\n ")
      guess = input()
      guess = int(guess)        

      guesses_taken += 1

      if guess < number:
          print("Incorrect, try again whit a higher number \n")
      elif guess > number:
          print("Incorrect, try again whit a lower number \n")
      elif guess == number:
          break
      

    def play_again():
      print("do you want to play again?")
      answer = input('Y: Yes, N: No ')
      if answer == 'Y' or 'y':
          high_low_game()
      elif answer == 'N' or 'n':
          print("Come back to play again someday!")
          return False
      else:
          print("That choice in not in the choice list") 
          play_again()           

    if guess == number:
        print(f"Correct!! Conrgratulations {username}, you won this game in {str(guesses_taken)} attempts!!")
        play_again()
    else:
        print(f"To bad, you miss the game, I was thinking in {number}")
        play_again()
          
high_low_game()