print("Hello World")
print("my name is Alice")
print("my age is 24.")
print("i have two apples","but ill give one to you.")
print(25)
print(30+30)
name = "Nancy" #string
age = 24 #int
weight = 55 #float
print("my age is:", name)
print("my age is:", age)
print("my weight is:", weight)
age2 = age 
print(age)
print(type(name))
print(type(age))
print(type(weight))
old = False  #boolean 
a = None #NoneType
print(type(old))
print(type(a))
print("this is :", old)
a = 2
b = 2
sum = a + b 
print(sum)
c = 1000
d = 500 
diff = c-d
print(diff)
print("my first python program with the help of freecodecamp") 

#ARITHMETIC OPERATORS 
a = 5
b = 5 
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) # MODULUS OPERATOR GIVES REMAINDER
print(a**b) #POWER OPERATOR -> a to the power b (a^b)

#relational/comparison operators
a = 50
b = 20
print(a==b) #EQUALS TO (FALSE)
print(a!=b) #NOT EQUALS TO (TRUE)
print(a >= b) #GREATER THAN OR EQUALS TO (TRUE)
print(a<=b) #LESS THAN OR EQUALS TO (FALSE)

#ASSIGNMENT OPERATORS
num = 10
num = num + 10
print("num:",num)
num = 10
num += 10 #ASSIGNMENT OPERATOR
print("num:",num)
num -= 10 #ASSIGNMENT OPERATOR
print("num:",num)
num = 10
num**=5 # POWER ASSIGNMNET OPERATOR
print("power is:", num)
num = 10
num %= 5 #MODULUS ASSIGNMENT OPERATOR 
print("remainder is :",num)
  
#LOGICAL OPERATORS NOT, AND, OR
print(not False)
a = 50
b  = 20
print(not(a > b)) #NOT LOGICAL OPERATOR / FLIPS THE VALUE
print(not(a<b))
 
val1 = True
val2 = True
print("and operator is:", val1 and val2) #AND LOGICAL OPERATOR
val1 = True
val2 = False 
print("this and value is:", val1 and val2)

val1 = True
val2 = False
print("this value is ORed is:", val1 or val2) # OR LOGICAL OPERATOR

a = 50
b = 40
print("OR operator is:", (a == b) or (a > b ))

# TYPE CONVERSION
#IMPLICIT TYPE CASTING / AUTOMATIC
a = 5 #int
b = 4.25 #float 
c = a + b
print(c)
#EXPLICIT TYPE CASTING / MANUAL
a = "2" #string
b = 5
a = int("2") #int because of explicit type casting
print(type(a))
print(a + b)

#INPUT() IN PYTHON
#INPUT STATEMENT IS USED TO ACCEPT VALUES (USING KEYBOARD) FROM THE USER
input("enter your name:")
print("welcome",name)
rollnumber = input("your roll number is:")
print("you entered:", rollnumber) #INPUT GIVES STRING VALUE BACK SO WE USE TYPE CASTING

name = input("enter your name:")
age = int(input("enter your age:"))
marks = float(input("enter your marks:"))
print("Welcome:",name)
print("age =", age)
print("marks",marks)

#PRACTICE/TEST QUESTIONS
val1 = int(input("enter first value:"))
val2 = int(input("enter second value:"))
print("total is:", val1+val2)

#SECOND QUESTION PRACTICE 
side = float(input("enter the side of the square:"))
print("area =", side * side)

#THIRD PRACTICE QUESTION 
a  = float(input("enter first value"))
b = float(input("enter second value"))
print("total average is:", (a+b)/2) #FORMULA OF AVERAGE  A PLUS B UPON/DIVIDED BY 2

#FOURTH QUESTION
a = int (input("enter your first value"))
b = int(input("enter your second value"))
print(a >= b)











