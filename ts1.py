#Ask your name
greeting = input("Hello what is your name:  ")
#Print your name with the respond
answer = print("Hello " + greeting)
#The currency
shopkeeper = print("I will be your shopkeeper.This is the items.The item will be in dolars")
#The set which contains the list of items
listofitems = {
                            
 "Milk" : 55,

"Honey" : 250,
 
"Eggs" :  300,

"Bread" :  50,

"Spinach" : 10,

"Towel": 256,

"Soda" : 50
}
print(listofitems)
#Asks you your first item
item1 = listofitems[input("What is your first item: ")]
print(item1)
#Asks you your second item
item2 = listofitems[input("What is your second item: ")]
print(item2)
#Asks you your third item
item3 = listofitems[input("What is your third  item:  ")]
print(item3)
#The total of the items
total = item1 + item2 + item3 

newTotal = int(total)


#The bill
print("Your total is " + str(total))






#What you want to pay
amount = input("Enter the amount you want to pay:  ")

change = int(amount) - newTotal
 
#Your change
print("change you'll recieve " + str(change))