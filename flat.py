#this is an example of a flat list there are also nested lists but we'll start with flats since they take up less space and are easier to read
#if you start with a certain number of entries, you need to have an equal number of keys to go along with them

flat_contacts= { #we assign our dictionary the variable name flat_contacts and the { represents the start of our dictionary
  "Name": ["Joshua", "Tom", "Sarah"], #in lists we have two different sections keys and values everything on the left side of the : is a key and the other side holds values 
  "Birthday": ["1/22/1997", "3/29/1998", "8/14/2000" ], #Birthday is a key and the dates are values
  "Number": ["(800)945-1100", "(800)934-7532", "(800)543-2100"], #Number is the key and the phone numbers are the values
  "Email": ["joshua@example.com", "tom@example.com", "sarah@example.com"] #Email is the key and the values are the emails
} #represents the closing of our dictionary 

#now its time to pull information from our dictionary remember python doesnt count in the 
#traditional sense we start from 0 and work upwards ill print the indexed list below
# Joshua = 0, Tom = 1, Sarah = 2
print(flat_contacts["Name"][0]) #If we want the name of the first person on the list we'd select the key(Name) and the indexed value 0
print(flat_contacts["Number"][0])#same for any other information stored in our dictionary

#we can add to our dictionary without directly accessing the dictionary as well
flat_contacts["Address"] = ["4302 Main St", "5630 Elm St", "2109 Oak St"]  # we create a new key called address and add the corresponding values 
print(flat_contacts)

#if we need to delete an input we'd use the built in function del
del flat_contacts["Email"]  #we are targeting the email address key specifically in this line

#if we need to update a pre existing entry in our dictionary we can using the following function
flat_contacts["Address"] = ["123 Main St", "456 Elm St", "789 Oak St"]  # Add a new key-value pair
flat_contacts["Name"][0] = "Josh" #we are targeting the 0 indexed value in the names key and changing it from Joshua to josh
print(flat_contacts)

#a common occurrence we'll see when working with larger dictionaries is a need to print a specific row 
# Since we have deleted the 'Email' key, we are commenting the below lines to prevent errors.
# emails = flat_contacts["Email"] #we create a variable that is equal to the row of emails in the dictionary
# print(emails)
#the same concept for targeting specific entries in the dictionary by using the index values applied
# print(emails[0]) #here were using our variable to access the dictionary specifically the row called emails and specify the entry were looking for by using the index values 

#lets say we inherit a large dictionary and arent familiar with all the information stored inside we have a few different options 
keys = flat_contacts.keys()#the first of which is creating a variable that contains the various keys in our dictionary 
print(keys)#this will print only the keys in our dictionary those will be (Name, birthday, address, number and email)
values = flat_contacts.values()#here were doing the same thing but only getting the values 

#the use of variables help us navigate through our dictionaries with ease 
josh = flat_contacts["Address"][2]
