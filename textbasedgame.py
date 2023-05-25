import random as random #the import feature allows us to randomize our work when prompted

username = input("Enter your username: ")#a variable with the purpose of getting the users name via the input function
print("Welcome {}! You are the starting point guard for the Miami Heat.".format(username.title()))#we use the {} as a placeholder and the format function to place the users input in our string and the title function to capitalize the name

while True:#we use the while loop with a boolean to ensure that the inputs are valid if not the it will return the "Invalid input. Please try again." listed below
    plot = input("\nYour team is in the finals and needs your help to win. Can you do it? ")#we name our variable plot it asks a question and gives users the option to respond
#this takes into account the general expected responses and prints an appropriate response depending on the initial response
    if any(word in plot for word in ["Yes", "yes", "Yeah", "yeah", "okay", "Okay", "si"]):
        print("\nThank you {}! With your help, I'm sure we'll win.".format(username.title()))
        break# this stops the loop a loop ends once an appropriate response is received
    elif any(word in plot for word in ["No", "no", "Nope", "nope"]):
        print("\nThank you {} for trying anyways.".format(username.title()))
        break
#the else is where our while loop plays an important role if we recieve an unexpected 
#response it restarts the process from the plot variable
#not displayed here but else cant accept an input function but "elif" and "if" can)
    else: 
        print("\nInvalid input. Please try again.")

print("\nYour opponents are the Denver Nuggets, you are currently down 114 to 112 with 7 seconds left in the 4th.")

game_over = False #variable with the boolean value of false meaning game is not over 
#the loop we create now continues to run as long as the game is not over
while not game_over:
#we provide users with three different scenarios
    print("\nChoose from the options below:") #you'll see us use the \n a few times its used to creeate a line break 
    print("1. Backdoor screen to Bam Abadeyo 63% success rate and ties the score at 114")
    print("2. Walk down pull up three 45% success rate but wins the game with the score at 115 to 114")
    print("3. Drive and kick out to Gabe Vincent with a 40% chance of turnover, 85% success rate if pass completed")
#then prompt users to choose from one of the three options below by selecting a number
    choice = input("\nEnter your choice (1-3): ") #create a new variable called choice which takes into account our users response
#the == checks to see if the values are equal to one another and returns a boolean value
    if choice == "1": #if the users choice equals 1 
        success = random.random() <= 0.63  # we run the random number generator and assign it the value of less than or equal to 0.63
        if success: 
            print("\nBam makes a 360 windmill dunk The score is tied at 114.")#if the random number generator lands on a number higher than 0.63 we print this 
        else:
            print("\nThe pass is stolen by Bruce brown, who runs out the rest of the clock heat lose.")
        game_over = True #if it lands on a number over 0.63 we print the string above and end the game. 
#this just repeats the process above but with different options and a different likelihood
    elif choice == "2":
        success = random.random() <= 0.45  
        if success:
            print("\n{} hits a pull up three the crowd roars!!! The HEAT ARE NBA CHAMPIONS!".format(username.title()))
        else:
            print("\n{} misses a pull up three, and Denver does it! The Nuggets WIN!!!".format(username.title()))
        game_over = True
#this block is slightly different from the rest as it has two different calls for the random number generator
    elif choice == "3": #if the users input is equal to 3 then the boolean is true and we start running the script
        turnover = random.random() <= 0.30  # we set the likelihood of a turnover occurring to be less than or greater than 0.30
        if turnover: #if the number is greater than 0.30 then we run the following script and end the game
            print("\nDrive and kick out to Gabe Vincent results in a turnover. Your team loses the game.")
            game_over = True
          #if not we proceed to run the next script and use the random number generator again 
        else:
            success = random.random() <= 0.85  # if the random number generator provides a number under 0.85 the user wins the game.
            if success:
                print("\nDrive and kick out to Gabe Vincent is successful! Your team wins the game at 115 to 114.")
            else:
                print("\nDrive and kick out to Gabe Vincent is missed.") # because this is our last valid conditional the game ends regardless of the outcome. 
            
            play_again = input("\nDo you want to play again? (Yes/No) ")
            if play_again.lower() not in ["yes", "y"]:
                game_over = True
            else:
                game_over = False
    #if the user enters a number not given in our instructions we print the following and allow them to try again.
    else:
        print("Invalid choice. Try again.")
print("\nThanks for playing, {}!".format(username.title()))  # regardless of the outcome we print the following that serves as an exit message 