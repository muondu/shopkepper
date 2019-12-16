a = input("Hello what is your name:  ")

b = print("Hello " + a)

c = print("I will be your shopkeeper.This is the items.The item will be in dolars")

t = {
                            
 "Milk" : 55,

"Honey" : 250,
 
"Eggs" :  300,

"Bread" :  50,

"Spinach" : 10,

"Towel": 256,

"Soda" : 50
}
print(t)
k = t[input("What is your first item: ")]
print(k)

l = t[input("What is your second item: ")]
print(l)


m = t[input("What is your third  item:  ")]
print(m)

n = k + l + m 

o = str(n)
print("Your total is " + o)

p = input("Enter the amount you want to pay:  ")


q = o - n
 

print("Your change is " + q) 