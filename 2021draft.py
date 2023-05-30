import pandas as pd #the pandas libary is one we use when building dataframes

#--------------this is our dictionary of four receivers from the 2021 draft-----------------
receiverclassof2021 = {
  "Team": ["Cincinnati Bengals", "Philadelphia Eagles", "Miami Dolphins", "New York Jets"],
  "Player": ["Jamar Chase", "DeVonta Smith", "Jaylen Waddle", "Elijah Moore"],
  "Draft picks": ["1st round Pick 5", "1st round Pick 10", "1st round Pick 6", "1st round Pick 18"],
  "2021 GP": [16, 17, 16, 17],
  "2021 receptions": [81, 64, 65, 53],
  "2021 Targets": [145, 104, 104, 93],
  "2021 TDs": [13, 6, 6, 4],
  "2022 GP": [17, 17, 17, 17],
  "2022 receptions": [81, 64, 104, 62],
  "2022 Targets": [139, 144, 165, 115],
  "2022 TDs": [13, 8, 6, 4],
}
#if we were to print(recieverclassof21) it would appear in the terminal in the format of a dictionary


#-------------------------converting our dictionary to a dataframe----------------------------------------------------------------
df = pd.DataFrame(receiverclassof2021)# we create a variable called df(dataframe) and use the pd.DataFrame() function to store our dictionary 
print(df) #now our work appears in a neat format but a few of our values are being cut off hence the ...
pd.set_option('display.max_columns', None) 
print(df) #now our work appears in a format where we can see everything


#-------------------------Manipulating the data frame-------------------------------------------------------------
#lets start with the loc function the loc function uses the index number to pull information associated with the key
print(df.loc[0]["Team"]) #here we are targetting the team name of the person in index value 0 (Jamar Chase)
print(df.loc[0]) #this gets all the information associated with the person in index number 0

# using this function will allow us to compare the values inside our dataframe against one another
print(df.loc[:, ["Player", "Total receptions", "Total TDs"]]) #the : allows us to select multiple rows


Devonta_Smith_TDs = df.loc[df["Player"] == "DeVonta Smith", "2021 TDs"].values[0]


#this adds a new row to our dataframe that adds the amount of TDs for 2021 and 2022 and provides us the total
df["Total TDs"] = df["2021 TDs"] + df["2022 TDs"]
print(df["Total TDs"])
df["Total receptions"] = df["2021 receptions"] + df["2022 receptions"]
print(df["Total receptions"])

#
Devonta_Smith_TDs = df.loc[df["Player"] == "DeVonta Smith", "2021 TDs"].values[0]

Jaylen_Waddle_TDs = df.loc[df["Player"]=="Jaylen Waddle", "2021 TDs"].values[0]
#now we start to work with our new variables, and conditional statements 
if Devonta_Smith_TDs > Jaylen_Waddle_TDs:
    print("Devonta Smith had more touchdowns than Jaylen Waddle in 2021.")
elif Devonta_Smith_TDs == Jaylen_Waddle_TDs:
    print("Devonta Smith and Jaylen Waddle had the same number of touchdowns in 2021.")
else:
    print("Jaylen Waddle had more touchdowns than Devonta Smith in 2021.")






