#import this 
# this is an example of a variables holding a value the variable is a and the value is 4
#remember python is case sensitive so A and a are two different variables
a = 4
# Values can be combined to do some cool things as well 
a = 4
b = 4
ab = a + b
print(ab) # print is considered a function that shows the value of what we have in parentheses to the console
#you could achieve the same result by doing 
print(a + b)

#lets start working with data types the most common is strings
#we can create strings using single or double quotes for one line strings and triple quotes for multiline strings 
#most things written inside the quotes are taken literally with a few exceptions which we'll see later
name = "my name is thomas"
print(name) 
#we can combine strings as followed
greeting = "hi joshua, "# remember to add a space before the end quotes
print(greeting + name)
# we could also use one of the following two methods
print("hi joshua, "+ "my name is thomas")
print("hi Joshua,", "my name is thomas")
# Accessing a specified character in a string
a = "Hello, World!"
print(a[9])
print(a[-1])
print(len(a))

# Now for the remaining data types
a = 4.0    # floats: are numbers with decimals fun fact if we divide in #python the answer is always a float   
c = 7      # integers(int) are whole numbers such as 1, 47, 1009.
e = True   # booleans(bool) are values can either be true or false
f = False 
#if we want to convert a data type to a different type we use the following function
print(float(7))
print(bool(7))
print(int(7))
print(str(7))  #the str is short for string like bool is for boolean or int for integer
#if we wanted to see the type of data type we were working with we'd do this
print(type(7))

# these are tuples, they can only hold multiple data types and are immutable meaning once we establish them we cant change it
car_year_brand = ("mustang", "ford", 1997 )
print(car_year_brand) #prints all entries in our tuple
#python doesn't count the same way we usually do in our tuple mustang would be 0 audi would be 1 and bmw would be 2
#if we want to print a specific value from our tuple we'd use the following method 
print(car_year_brand[2])
#if we wanted to print everything inside the tuple we'd use the following
for car_year_brand in car_year_brand: # think of the for as saying "for every car year or brand in our tuple print car"
    print(car_year_brand)


# Next are lists, list are similar to tuples but they're mutable meaning we can add and remove values
Browns= ["Martin Emerson Jr", 23, "Denzel Ward", 21, "Greg Newsome", 20]
print(Browns)#prints our new list 
print(Browns[2])#prints number 2 in our list of browns Denzel Ward
Browns[0] = "Cam Mitchell" #inserts an entry to our list at the specific position
Browns.insert(6, "Rodney Mcleoud") #another way to insert an entry to our list at a specific position
Browns.append("Juan Thornhill") #inserts an entry to our list at the end of our list
print(Browns)
# a few ways to remove an items from a list
Browns.pop(0)# another built in function that targets an indexed position in the list and removes it
Browns.remove("Juan Thornhill")# a built in function that removes a specified entry from the list
print(Browns)

# above we saw one way to build a list this is another
flowers = [] #if you were to do print(flowers) it would display a empty list but
flowers.append("Roses")# now it would display a list consisting of roses
flowers.append("Sun flower")# now it would display a list consisting of roses and sun flower
flowers.append("Tulip")#now it would display a list consisting of roses, sun flowers and tulips
flowers.append("Orchid")#please don't make me type that full thing out again
##if you noticed our list when printed to the terminal have brackets around them below is how we remove them
print(", ".join(flowers))

#Now we can start to see how everyting we've learned thus far is combining our list with strings
flowers = ["Roses", "Tulips", "Orchids"]
flowers = ("I bought my mom " + flowers[2] + " she loved them.")
print(flowers)


#earlier i mentioned that there were exemptions to the rule that everything 
#inside our string is taken literally here is the fist exception
age = 37 #we start by creating a variable that holds the value of an integer 
#called age and another called birthday_congrats
birthday_congrats = ("Hi, Happy birthday congrats on making it to {}".format(age))
#the {} serves as a placeholder for the age variable and at the end the function format lets us know what variable is going to be in the placeholder
print(birthday_congrats)
#another way to do this would be Type conversion although age is an integer by using type conversion we make it a string and more compatible
age = 37# we create a variable that holds an integer but change it using type conversion
birthday_congratulations = ("Hi, Happy birthday" + " you're finally " + str(age))
print(birthday_congratulations)
age = 37 # we create a variable that holds an integer then use the f string format 
birthday_congratulations = f"Hi, Happy birthday! Congrats on making it to {age}."
print(birthday_congratulations)

# time to start with conditional statements, conditional statements are exactly what they sound like
#they provide different options based on the results
#  == checks to see if equal to
# not equal to !+ checking for inequality
# <= less than or equal to
# >= greater than or equal to
# > greater than
# < less than
x = 8
y = 7
w = 6
print(x > y)
print(x==y)
print(x < y)
print(w < y ==x )
# lets try with a simple algorithm we create a variable called height that holds the float 6.0
height = 6.0
#now we add an if statement if our variable height is greater than or equal to 6.0 print you are tall
if height >= 6.0:
    print("You are tall.")
else:
    print("You are not tall.")
# Lets say we want to communicate with users in the terminal we use Input/Output functions
#when we add an input function to our variable we created the option to add information in the terminal
name = input("What is your name? ")
#this may look familiar from earlier in line 19 we briefly went over the concept.
print("Hello " + name + "!")
#another example of this would be what we looked over in line 85
inquiry = input("What school do you go to now ? ")
print("wow {}, has a beautiful campus".format(inquiry))

#python is easier to work with once you learn the fundamentals and continue to build on them 
# above we learned about the input and output functions as well as conditionals this is how we'd use them together
Brittany_appointment = "not scheduled"
if Brittany_appointment == "10:30":
    print("Brittany's appointment is at 10:30")
elif Brittany_appointment == "not scheduled": #we use elif if more than one option think of it as else if
    response = input("Brittany's appointment is not scheduled. Would you like to schedule one now? ")
else:
    print("Brittany's appointment is at 11:30, not 10:30")
#lets discuss while loops and break our code down line by line
count = 0 #we create a variable with the integer 0 
while count < 5: #then add a while loop that says while our variable count is less than 5 
    print("Count is: ", count) #print the "Count is: " whatever the variable count is currently at
    count += 1  # count = count + 1 

#dictionaries are important in python its one way to hold information 
user_dataset = {
  "Thomas": {
    "age": "28",
    "height": "6'1",
    "weight": "167lbs",
    "race": "african american"
  },
  
  "Joshua": {
    "age": "23",
    "height": "6'0",
    "weight": "230lbs",
    "race": "african american"
  },

  "Brittany": {
    "age": "24",
    "height": "5'4",
    "weight": "137lbs",
    "race": "jamaican american"
  }, 
}
#the content inside the dictionary is broken down into two parts keys and values for example
#Joshua is the key in this dictionary while height and age are the values being nested in the dictionary
#to access specific keys and values in our dictionary we use the following functions in this case joshua is the key and age is the value
print(user_dataset["Joshua"]["age"])
#if i wanted all the information on joshua in our dictionary id use the following function
print(user_dataset.get("Joshua"))
#this is how you delete an entry from the dictionary 
del user_dataset["Joshua"]
#this is how you print an entire dictionary 
print(user_dataset)

# Exception Handling
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a second number: "))
    print("a/b = " + str(a/b))
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input. Please enter a number.")
