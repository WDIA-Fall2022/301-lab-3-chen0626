import pylightxl as xl

with open('city.xlsx', 'rb') as f:
    db = xl.readxl(f)

l = list(db.ws(ws='Sheet1').col(col=3))
#print()

#ask the user for the code of the country and save it into a variable
countryCode = str(input("Enter your country code>"))

#Scan the list l line by line and add 1 to the counter if the country is the one looked for
#use for loop, each country is one loop

counter = 0
for i in l:
    if i == countryCode:
        counter += 1

#Format and print the result
print("{} matched".format(counter))

#Ask the user for the population looked for. Use a loop and a try except to validate the input as a valid integer

while(True):
            try:
                population = int(input("Enter the population > "))
            except:
                print("invalid population")
                continue
            else:
                break

#Store the population values into a list called l1 (see line 6)
l1 = list(db.ws(ws='Sheet1').col(col=5))

#Initialize a list lstOfRecords to an empty list
lsOfRecords=[]

#Scan the list l1, if the population is larger than the population looked for, add the list index to lstOfRecords
#listName.index(valueOrltem)

for i in range(len(l1)):
    if l1[i] > population:
        lsOfRecords.append(i)


#Print (lsOfRecord)
print(lsOfRecords)

#Bonus: Print the name of the cities whose index is in lsOfRecords
l2 = list(db.ws(ws='Sheet1').col(col=2))
for i in lsOfRecords:
    print (l2[i])
