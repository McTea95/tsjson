# Python program to read
# json file
  
  
import json
  
# Opening JSON file
f = open('tsjson/accounts.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)

# Iterating through the json
# list
#for i in data:
#    print(i)


while True:
    eingabe = (input("Bitte gebe alter oder Kontostand ein:\nquit um abzubrechen.\n"))
    if eingabe == "quit":
        print("Programm wird beendet...")
        break
    elif eingabe == "alter":
        for i in data:
            if i["age"] > 25:
                print(i["name"],"ist",i["age"],"Jahre alt.")    
    elif eingabe == "Kontostand":
        balance = [] #helping array data, filled from the json file

        for i in data: 
            balance.append(i["balance"]) #append the json file into the array

        highst = balance[0] #helping variblg to save the highst value

        for number in balance: #sorting
            if number > highst:
                highst = number
        print(highst)
    else:
        print("falsche Eingabe, versuche es erneut!")


# Closing file
f.close()