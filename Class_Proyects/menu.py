def diner():

  main_menu = {
    "pizza": ["Pizza", 2], 
    "tacos": ["Tacos", 2.50]
  }

  side_menu = {
    "fries": ["Fries", 1], 
    "tatertots": ["Tatertots", 1.50]
  }

  bill = 0

  # Display the menus
  #choose from the menus
  # Total their bill

  def greeting():
    print('Welcome to the python Diner!')
  
  def menu_display(menu):
    for item in menu.values():
      print(f'{item[0]} -> ${item[1]}')
  
  def user_selection(menu):
    while True:
      user_input = input("What item would you like?")
      menu_selection = menu.get(user_input, False)
      if menu_selection == False:
        print("I'm sorry, but that was not on the menu...")
        continue
      else:
        print(f'You picked {menu_selection[0]}, great choice!')
        return menu_selection[1]

  def checkout():
    print(f"Your bill today will be ${bill:.2f}")
    print("Thank you for dinning at the Python Dinner! Have a great day!")


  greeting()

  print('\nHere is the main menu:')
  menu_display(main_menu)

  bill += user_selection(main_menu)

  print('\nHere is the side menu:')
  menu_display(side_menu)

  bill += user_selection(side_menu)

  checkout()


diner()