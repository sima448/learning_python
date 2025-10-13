'''#type conversion
a = 4
b =34.6
sum = a + b
print(sum) #38.6

#a = "2"
#b = 23.67
#sum = a + b  # output error becouse string data ko  python me float data ke sath conversion nhi ho sakta, esko hm dusre trika se kr sakte he
a1 = int("12")
b1 = 23.3
sum1 = a1 + b1
print(sum1)#35.3

####
x = 3
x = str(x)
print(type(x))


# input in python
input("Enter your name: ")#sima

####
name = input("Enter your name: ") #sima
print("Welcome", name) # welcome sima
##
val = input("Enter the value: ")
print(type(val), val)# "2.3" ,"45"

##
val = int(input("Enter the value: "))
print(type(val), val)# 23,24.5


#Q1. write a program to input 2 numbers & print their sum.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter Second number: "))
sum = num1 + num2
print(sum)

#Q2. WAP to input side of a sequare & print its area
a = float(input("Enter the side: "))
print("area =", a*a)

#Q3. WAP to input 2 floating points numbers & print their average
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
avg = (x+y)/2
print(avg)
'''
#Q4. WAP to input 2 int numbers, a and b print true if a is greater than or equal to b.if not print false
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(a >= b)
'''if (a >= b):
    print("true")
else:
    print("false")
'''