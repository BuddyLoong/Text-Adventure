import jail_cell

#This is the print statment for the title screen
print("Text Adventure")
print("Options:\n1.Start\n2.Option\n3.Exit")

#user_option is a variable that stores.
#input is the user's input
#int and str are used to convert a string or intreger.
user_option = input("What do you want to do?1\\2\\3\n")
user_option = int(user_option)
#if depending on user input
#if, elif and else are used if there is different user's input choice.
#Different input will print out different statements
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
