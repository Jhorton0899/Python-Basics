import random

username = input("Enter your username: ")
print("Welcome {}! You are the starting point guard for the Miami Heat.".format(username))

while True:
    plot = input("Your team is in the finals and needs your help to win. Can you do it? ")

    if any(word in plot for word in ["Yes", "yes", "Yeah", "yeah", "okay", "Okay", "si"]):
        print("Thank you {}! With your help, I'm sure we'll win.".format(username))
        break
    elif any(word in plot for word in ["No", "no", "Nope", "nope"]):
        print("Thank you {} for trying anyways.".format(username))
        break
    else: 
        print("Invalid input. Please try again.")

print("Your opponents are the Denver Nuggets and you are currently down 114 to 112 with 7 seconds left in the 4th.")

game_over = False

while not game_over:
    print("\nChoose from the options below:")
    print("1. Backdoor screen to Bam Abadeyo 63% success rate and ties the score at 114")
    print("2. Walk down pull up three 45% success rate but wins the game with the score at 115 to 114")
    print("3. Drive and kick out to Gabe Vincent with a 40% chance of turnover, 85% success rate if pass completed")

    choice = input("\nEnter your choice (1-3): ")

    if choice == "1":
        success = random.random() <= 0.63  # 63% success rate
        if success:
            print("\nBam makes a 360 windmill dunk The score is tied at 114.")
        else:
            print("\nThe pass is stolen by Bruce brown, who runs out the rest of the clock heat lose.")
        game_over = True

    elif choice == "2":
        success = random.random() <= 0.45  # 45% success rate
        if success:
            print("\n{} hits a pull up three the crowd roars!!! The HEAT ARE CHAMPIONS AGAIN!".format(username))
        else:
            print("\n{} misses a pull up three, and Denver does it! The Nuggets WIN!!!".format(username))
        game_over = True

    elif choice == "3":
        turnover = random.random() <= 0.30  # 30% chance of turnover
        if turnover:
            print("\nDrive and kick out to Gabe Vincent results in a turnover. Your team loses the game.")
            game_over = True
        else:
            success = random.random() <= 0.85  # 85% success rate if complete
            if success:
                print("\nDrive and kick out to Gabe Vincent is successful! Your team wins the game at 115 to 114.")
            else:
                print("\nDrive and kick out to Gabe Vincent is missed.")
            game_over = True

    else:
        print("Invalid choice. Try again.")



print("\nThanks for playing, {}!".format(username))


