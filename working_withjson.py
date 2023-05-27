#This is a nested dictionary its important to get familiar with these because we'll see them the most while working with JSON's
contacts = {
  "Joshua" :{ 
  "Number": "(800) 643-2184",
  "Email": "Joshua@example.com",
  "Address": "322 SW Main St"
},
  "Tom": {
    "Number": "(800)-432-1837",
    "Email": "Tom@example.com",
    "Address": "122 E love Blvd"
  },
  "Lisa" : {
  "Number": "(435) 643-7917",
  "Email": "Lisa@example.com",
  "Address": "211 W weston St"
  }
}

#we can use the following to retrieve specific information from our dictionary 
print(contacts["Joshua"])#this pulls the key joshua from the dictionary and returns all of the associated values

print(contacts["Joshua"]["Address"])#this code goes to the key joshua and pulls the address from the dictionary

#we use the del function to delete parts of our dictionary
del contacts["Joshua"]# here we are removing the key joshua and all associated values from the dictionary
del contacts["Lisa"]["Email"] # here we are removing just the email associated with Lisa but leaving her other values intact



#------------------------Converting a JSON to a dictionary------------------------
import json # we use the import function to let our IDE know that we're working with a json

# we make a variable called json_str that holds the value of our initial json
json_str = '''
{
  "Joshua": {
    "Number": "(800) 643-2184",
    "Email": "Joshua@example.com",
    "Address": "322 SW Main St"
  },
"Tom": {
    "Number": "(800)-432-1837",
    "Email": "Tom@example.com",
    "Address": "122 E love Blvd"
  },
    "Lisa" : {
    "Number": "(435) 643-7917",
    "Email": "Lisa@example.com",
    "Address": "211 W weston St"
  }
}
'''

# We create a variable called contacts that holds our converted JSON
contacts = json.loads(json_str) #the json.loads() function turns our json to a dictionary

# from here we can access our data like we would any other dictionary
print(contacts["Joshua"]["Number"])   # Output: (800) 643-2184
print(contacts["Joshua"]["Email"])    # Output: Joshua@example.com



#------------------Converting a dictionary to a JSON--------------------------------------------------------------
import json 
#we start with our dictionary that holds a list of contacts
contacts = {
    "Joshua": {
        "Number": "(800) 643-2184",
        "Email": "Joshua@example.com",
        "Address": "322 SW Main St"
    },
    "Tom": {
        "Number": "(800)-432-1837",
        "Email": "Tom@example.com",
        "Address": "122 E love Blvd"
    },
    "Lisa": {
        "Number": "(435) 643-7917",
        "Email": "Lisa@example.com",
        "Address": "211 W weston St"
    }
}

json_str = json.dumps(contacts)# we use the json.dumps() function to convert our dictionary to a json object with the variable name json_str
print(json_str)
