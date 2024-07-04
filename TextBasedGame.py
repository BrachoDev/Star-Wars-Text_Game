# Carlos Bracho

# Figures
figure_intro = """
.        .          .    .    .            .            .                   .
               .               ..       .       .   .             .
 .      .     T h i s   i s   t h e   g a l a x y   o f   . . .             .
                     .              .       .                    .      .
.        .               .       .     .            .
   .           .        .                     .        .            .
             .               .    .          .              .   .         .
               _________________      ____         __________
 .       .    /                 |    /    \    .  |          \\
     .       /    ______   _____| . /      \      |    ___    |     .     .
             \    \    |   |       /   /\   \     |   |___>   |
           .  \    \   |   |      /   /__\   \  . |         _/               .
 .     ________>    |  |   | .   /            \   |   |\    \_______    .
      |            /   |   |    /    ______    \  |   | \           |
      |___________/    |___|   /____/      \____\ |___|  \__________|    .
  .     ____    __  . _____   ____      .  __________   .  _________
       \    \  /  \  /    /  /    \       |          \    /         |      .
        \    \/    \/    /  /      \      |    ___    |  /    ______|  .
         \              /  /   /\   \ .   |   |___>   |  \    \\
   .      \            /  /   /__\   \    |         _/.   \    \            +
           \    /\    /  /            \   |   |\    \______>    |   .
            \  /  \  /  /    ______    \  |   | \              /          .
 .       .   \/    \/  /____/      \____\ |___|  \____________/  
                               .                                        .
     .                           .         .               .                 .
                .                                   .            .
"""

figure_good_end = """
          .                            .                      .
  .                  .             -)------+====+       .
                           -)----====    ,'   ,'   .                 .
              .                  `.  `.,;___,'                .
                                   `, |____l_\\
                    _,.....------c==]""______ |,,,,,,.....____ _
    .      .       "-:______________  |____l_|]'''''''''''       .     .
                                  ,'"",'.   `.
         .                 -)-----====   `.   `.              
                     .            -)-------+====+       .            .
"""

figure_bad_end = """

                       .-.
                      |_:_|
                     /(_Y_)\\
.                   ( \/M\/ )
 '.               _.'-/'-'\-'._
   ':           _/.--'[[[[]'--.\_
     ':        /_'  : |::"| :  '.\\
       ':     //   ./ |oUU| \.'  :\\
         ':  _:'..' \_|___|_/ :   :|
           ':.  .'  |_[___]_|  :.':\\
            [::\ |  :  | |  :   ; : \\
             '-'   \/'.| |.' \  .;.' |
             |\_    \  '-'   :       |
             |  \    \ .:    :   |   |
             |   \    | '.   :    \  |
             /       \   :. .;       |
            /     |   |  :__/     :  \\
           |  |   |    \:   | \   |   ||
          /    \  : :  |:   /  |__|   /|
          |     : : :_/_|  /'._\  '--|_\\
          /___.-/_|-'   \  \\
                         '-'   

"""

# Intro Text
text = """
        You are a young Jedi who escaped Order 66 a few years ago.
       You have been helping the Rebels at one of their secret bases
            located on a planet called Dantooine; However, the
   Galactic Empire has taken over the base, and Darth Vader is blocking
 the hangar, waiting for you. To escape, you need to collect all the
necessary items before facing Vader. Retrieve a holocron from the archives
  room to learn about Vader’s weaknesses, an old Mandalorian armor from
    the barracks to protect your body, a lightsaber from the training room
   to combat Vader, a shield generator from the tech lab, a grappling hook
 from the supply room to maneuver around the hangar, and finally, a ration
pack from the mess hall to gather enough energy to defeat Vader and escape
                                 Dantooine.
"""

# GLOBAL VARIABLES:

inventory = []
separator = "------------------------------------------------------------------------------------"
current_room = "Resting Quarters"
move = []
rooms = {
'Resting Quarters' : { 'East' : 'Mess Hall'},
'Mess Hall' : {'North' : 'Tech Lab', 'East': 'Barracks', 'South' : 'Supply Room', 'West' : 'Resting Quarters', 'item' : 'Ration Pack'},
'Tech Lab' : {'East' : 'Archives Room', 'South' : 'Mess Hall', 'item' : 'Shield Generator'},
'Archives Room' : {'West' : 'Tech Lab', 'item' : 'Holocron'},
'Barracks' : {'West' : 'Mess Hall', 'North' : 'Training Room', 'item' : 'Mandalorian Armor'},
'Training Room' : {'South' : 'Barracks', 'item': 'lightsaber'},
'Supply Room' : {'North' : 'Mess Hall', 'East' : 'Hangar', 'item' : 'Grappling Hook'},
'Hangar' : {'West': 'Supply Room', 'item': 'Vader'}
}

# FUNCTIONS :

# function showing the goal of the game and move commands
def show_instructions():  
  print(figure_intro)
  print(text)
  print("INSTRUCTIONS:\nMove commands: go South, go North, go East, go West")
  print("Add to Inventory: get 'item name'")

# Player's status function:
def status():
  global move
  print(separator)
  print(f"You are in the {current_room}")
  print(f"Inventory: {inventory}")

  # Using Conditional to display artifact if there is one
  if 'item' in rooms[current_room]:
    print(f"You see a {rooms[current_room]['item']}")
  
  move = input("Enter your move: ").split(maxsplit=1)

# Function to get item in room and remove it from the rooms dictionary:
def get_item():
  if 'item' not in rooms[current_room]:
    print("There is nothing to pick up here.")
  elif move[1] != rooms[current_room]['item']:
    print("That artifact is not here!")
  elif move[1] == rooms[current_room]['item']:
    inventory.append(rooms[current_room]['item'])
    del rooms[current_room]['item']


# Main function
def main():
  global current_room, move

  while current_room != 'Hangar':

    # Player's Status
    status()
    
    # Conditional to move between rooms
    if move[0] == "go" and move[1] in rooms[current_room]:
      current_room = rooms[current_room][move[1]]

    # Conditional for invalid direction
    elif move[0] == "go" and not move[1] in rooms[current_room]:
      print("You can't go that way!")

    # Conditional to get artifact
    elif move[0] == "get":
      get_item()

    # Conditional for invalid input
    else:
      print("Invalid move. Try again")
  
  #Conditionals to validate if player won or lost
  if len(inventory) == 6:
    print(separator)
    print("\nEmpowered by the artifacts you found,\nyou confronted Darth Vader and emerged victorious in an epic showdown.\nWith the Sith Lord vanquished, you took a starship and escaped from Dantooine just in time.\nVictory is yours, but you know Vader will strike back....")
    print(figure_good_end)
    print("YOU WIN\nThank you for playing my game!!!")

  else:
    print(separator)
    print("Despite you valiant efforts, Vader's overwhelming power proved to be too much for you.\nyou find yourself now a captive aboard the Death Star,\na prisoner of the Empire")
    print(figure_bad_end)
    print("Game Over\nThank you for playing my game!!!")

  exit_command = True

  while exit_command == True:
    exit_input = input("\nType 'exit' to leave the game\n")
    if exit_input == 'exit':
      exit_command = False

show_instructions()
main()