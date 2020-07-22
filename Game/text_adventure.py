import jail_cell

#This is the print statment for the title screen
print("Text Adventure")
print("Options:\n1.Start\n2.Option\n3.Exit")
user_option = input("What do you want to do?\t(1\\2\\3)\n")
user_option = int(user_option)
#if depending on user input
if (user_option == 1):
    print("You wake up in a dark cell.")
    jail_cell.start_game()
elif (user_option == 2):
    print("1.Text Colour")
    print("2.Text Size")
    print("3.Back")
elif (user_option == 3):
    print("Exit Game")
else:
    print("This is not an Option")
