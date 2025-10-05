
#double quote ke sath koi bhi values denge vo as a string output dega.
print("Hellow World")
print("my ma,eis Sima.")
print("My age is 19.")
print("this is my book","this is not yours")
print("45")
print("24+2")
print(24 + 5)

# define variables
name = "suman" 
age = 17
price = 250.30
print(name) #print values without double quote,
print(name , age, price)# all values print  separate (,) 
print("your name is :", name)
print("your age is :", age)

# define variables ka type kya he use pata lgane k liye hm likhenge
print(type(name))
print(type(age))
print(type(price)) 

#int,boolean, none data type
age1 =24
old = False
a = None
print(type(age1))
print(type(old))
print(type(None))

#print sum of two number
a = 5
b = 6
sum = a + b
print(sum)

#print arithmetical (+, - , *, %, /)
x = 10
y = 4
sum = x + y
subtract = x - y
multiplay = x * y
modulus = x % y
division = x / y
print(sum)
print(subtract)
print(multiplay)
print(modulus)
print(division)

#string & numeric values can operator together with *
A, B = 3, 2
Txt = "@"
print(3 * Txt * 2) #output ->  @@@@@@

# string & string can operate with + means(concatenation)
A1, B1 = "2" , 4
Txt1 = "@"
print((A1 + Txt) * B1) #output -> 2@2@2@2@

#Numeric values can operate with all arithmatic operators

a2, b2 = 5, 6
c2 = 4
print(a2 + b2 * c2) # 29 output

#arithmatic expression with integer and float will result in float
A2, B2 = 40, 5.0 
C2 = A2 * B2
print(C2) # 200.0 output


#Result of division operator with two integers will be float
a3, b3 = 5, 2
c3 = a3 / b3
print(c3) 
 # 2.5 output

# Integer division with float and int will give int displayed as float
a4, b4 = 1.5, 2
c4 = a4 // b4 
print(c4, a4/b4) # c4 ka value 0 ho gaya matlab 0.0 show, because integer division 0.999 bhi aayega to usko 0 kr dega so that if 1.555 ko 1 kr dega , aur a4/b4 simple division tha esliye 0.75 show huaa

#floor given closest integer, which is lesser than or equal to the float value Result of (A//B) is same as floor(A/B)
a5, b5 = 5, 2
c5 = a5 // b5
print(c5) # 2

a6, b6 = -5, 2
c6 = a6 // b6
print(c6) # -3

a7, b7 = 5, -2
c7 = a7 // b7
print(c7) # -3"""

#singl line comment
"""triple quotetion , this is 
multi-line comment"""



#