current_bank_balance = [300]

def start():
  print("Hello and Welcome to the Bank")
  main_menu()

def main_menu():
  print("Here are our menu options")
  user_input = input("Please select from the following menu choices: 1: Deposit, 2: Balance, 3: Withdraw, 4: Make a bill payment, 5: Quit ")
  print(user_input)
  if user_input == "1":
    deposit()
  elif user_input == "2":
    balance() 
  elif user_input == "3":
    withdraw()
  elif user_input == "4":
    pay_bill()
  elif user_input == "5":
    print("Please come again")
  else:
    print("That is not a valid option, please try again")
    main_menu()

def deposit():
  deposit_amount = input("How much would you like to deposit?  ")
  current_bank_balance.append(float(deposit_amount))
  print(f'You have deposited {deposit_amount}')
  deposit_subchoice()

def deposit_subchoice():
  user_choice = input("Would you like to do another deposit? or return to the main menu? 1:Deposit, 2:Main Menu, 3:Quit   ")
  if user_choice == "1":
    deposit()
  elif user_choice == "2":
    main_menu()
  elif user_choice == "3":
    print("Please come again")
  else:
    print("That is not a valid option, please try again")
    deposit_subchoice()


def balance():
  print(f"Here is your current balance ${float(sum(current_bank_balance)):.2f}")

def balance_subchoice():
  user_choice = input("Would you like to do anything else? 1:Main Menu, 2:Quit")
  if user_choice == "1":
    main_menu()
  elif user_choice = "2":
    print("Please come again")
  else:
    print("That is not a valid option, please try again")
    balance_subchoice()
    

def withdraw():
  print("hi from withdraw")
  main_menu()

def pay_bill():
  print("hi from pay bill")
  main_menu()


start()