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

listconstructor = list()
input1 = int(input("How many items do you want do buy: "))
for b in range(input1):
    input2 = listofitems[input("What is your item:  ")]
    print(input2)
    

    listconstructor.append(input2) 

    total = sum(listconstructor)

#The bill
    print("Your bill is " + str(total))






#What you want to pay
amount = input("Enter the amount you want to pay:  ")

change = int(amount) - int(total)
 
#Your change
print("your change is " + str(change))