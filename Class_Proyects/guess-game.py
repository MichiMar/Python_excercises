def guessing_game():
  def input_checker(user_input, list_of_numbers):
    list_of_numbers.sort()
    list_length = len(list_of_numbers)

    if not user_input.isnumeric():
      return False

    user_input = int(user_input)

    if user_input < list_of_numbers[0] or user_input > list_of_numbers[list_length - 1]:
      return False

    return True


  nums = list(range(1, 100))
  nums_checker = nums.copy()

  while True:
    print('What is your guess?')
    guess = input()

    if not input_checker(guess, nums_checker):
      print("That is an invalid selection... Please try again")
      continue

    guess = int(guess)

    if guess == 42:
      print('You correctly guessed it!')
      break
    elif guess in nums:
      print(f"No, {guess} isn't the answer, please try again\n")
      nums.remove(guess)
    else:
      print(f"You already guessed {guess}... Please try again")

guessing_game()