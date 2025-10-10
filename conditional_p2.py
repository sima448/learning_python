# if,elif,else conditions
'''light = input("light color: ")
if(light == "red"):
    print("Stop")
elif(light == "green"):
    print("Go")
elif(light == "yellow"):
    print("Look")
else:
    print("light is broken")


#grades of student marks

marks = int(input("marks : "))
if (marks >= 90):
    print("A")
elif (marks >= 80 and marks < 90):
    print("B")
elif (marks >= 70 and marks < 80):
    print("C")
else:
    print("D")



#practice time
# A = 5 & G = M
# A = 2 & G = F
A = int(input("A : "))
G = input("M/F : ")
if((A == 1 or  A == 2) and G == "M"):
    print("fee is 100")
elif(A == 3 or A == 4 or G == "F"):
    print("fee is 200")
elif(A == 5 and G == "M"):
    print("fee is 300")
else:
    print("no fee")

# conditional Statements
#Single line if/ternary operator 
food = input("food : ")
eat = "Yes" if food == "cake" else "no"
print(eat) 

#######
food = input("food : ")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")


#clever if/ternary operator
# eska bahut kam use karte he . thoda complex expressions he
age = int(input("age : "))
vote = ("no", "yes") [age >= 18]
print(vote)



# simple interest
P = float(input("p : "))
r = float(input("r : "))
t = float(input("t : "))
si = (P*r*t)/100
print(si)


#relational operator
a = 20
b = 30
print(a == b)
print(a != b)
print(a >= b)
print(a > b)
print(a <= b)
print(a < b)


#assignment operator
num = 10
num = num + 10
print("num: ", num)

num = 10
num += 10
print("num: ", num)

num = 10
num -= 10
print("num: ", num)

num = 10
num *= 10
print("num: ", num)

num = 10
num /= 10
print("num: ", num)

num = 10
num %= 10
print("num: ", num)

num = 10
num **= 10
print("num: ", num)
'''
#logical operator

print(not True)
print(not False)
#ya
a = 30
b = 20
print(not (a > b))
print(not (a < b))
print("AND operator:", a == b and a > b)
print("OR operator:", a == b or a > b)


val1 = True
val2 = False
print("AND operator:", val1 and val2)
print("OR operator:", val1 or val2)
