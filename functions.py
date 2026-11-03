#                   Function 
# function is a reusable block of code do a task
# function run when you call it 
# function accept element to deal with called {parmeters}
# there is a built-in functions and user defined function
# function accept element when you called it {Arguments}
#               to build function 
#   def function name (parmeters or not)
 



def hellomessage() :  
    return " Hello World "
print (hellomessage())

#def name_(a):
#    return (a)
#for i in range(1,6) :
#    s=input(" Enter your name : ").strip()
#    print("Hello "+name_(s))

def add(a,b) :
    if type(a)==int and type(b)==int :
        return a+b
    else :
        print (" You enter wrong date ")
add(3,7)
    
def full_name(frist,second,last):
    if type(frist) == str and type(second) == str and type(last) == str :
        print (f"The full name is {frist.capitalize()} {second:.1s} {last.capitalize()}")
    else :
        print (" This input not string ")    
full_name("mohamed","hany","mohamed")


def show (*skiiils) :
    for name in showskills :
        print (f" Hello Mohamed your skills is {name}")

showskills=["cpp","python","html"]

show(*showskills)

#       function default parameter 
def mee(name,age,country):
    print(f" My name is {name.title()} , my age is {age} and iam from {country}")

#namee=input(" Enter your name ".capitalize())
#agee=int(input(" Enter your age "))
#countryy=input(" Where are you from ? ")
#mee(namee,agee,countryy)

#       function scope 

#x=1 #Global scope

#def one ():
#    print (f" print variable from function scope {x} ")
#print (f" print variable from global scope {x} ")    
#one()



def one ():
    x=1
    print (f" print variable from function scope {x} ")

#print (f" print variable from global scope {x} ")    # x is not global variable
one()

def one ():
    global x # to  change the variable form local to global   
    x=1
    print (f" print variable from function scope {x} ")


#       function Recursion

def cleanword(word):
    if len(word)==1:
        return word
    if word[0]==word[1]:
        return cleanword(word[1:])
    return word[0]+cleanword(word[1:])

print (cleanword("wwwwooorrrllldd"))

#           lambda function
#   it han no name 
#   you can call it inline without defining it 
#   lambda date type is function
#   lambda is one singel expression not block of code  
#   you can use it in return date from anthor function


def say_hello(name,age): return f" hello {name} your age is : {age}"
hello=lambda name,age :  f" hello {name} your age is : {age}"

print (say_hello("mohamed",19))
print (hello("mohamed",19))

print (type(say_hello))
print (type(hello))

print (say_hello.__name__)
print (hello.__name__)


#           built in function
# all()
# any()
# bin()
# id ()
# sum(iterable,start) start added to sum 
# round(number,numofdigits) num of digits -> el rakm el 3ashri
# range(start ,end, step) end -> egbary
# print()
# abs()
# max()
# min()
# pow()
# slice()
# enumerate(iterable,start=0)
# help()
# reversed

x=[1,2,3,4]
if all(x):
    print (" All elements is True ")
else:
    print (" There is at least one element is False ")

y=[0,1]
if any(y):
    print (" There is at least one element is True")
else:
    print (" There is no any True element ")

print (bin(100)) # binary


a=1
print (id(a)) # address 


lis=[1,20,9,10]
print (sum(lis))
print (sum(lis,5))

print (round(15.499))
print (round(15.5))
print (round(15.4994,3))

print (list(range(10))) # from 0 ->9
print (list(range(0,10,2))) #  even 
print (list(range(1,10,2))) #  odd 

print (" hello","mohamed","how","are","you",sep=" $ ")

print(abs(100))
print(abs(-100))
print(abs(10.19))
print(abs(-10.19))

print(pow(2,3))#  (2*2*2)
print(pow(2,3,2))#  (2*2*2)%2

#. x=[1,2,3,4]
print(min(10,2,0,-18,19))
print (min(x))

#. x=[1,2,3,4]
print(max(10,2,0,-18,19))
print (max(x))

print ("#"*50)
skills=["cpp","python","html","css"]
skillscounter=enumerate(skills,1)
for skill in skillscounter:
    print (skill)

print ("#"*50)
tup=(1,2,3,4,5)

print (reversed(tup))
for num in reversed(tup):
    print (num)





#           map()
# map take function and iterator
# map called map because it map the function on every element
# the function can be pre-defiend function or lambda function

def foramatetext(text):
    return f"_  {text}  _"
mytext= ("mohamed","osama","ali")
myforamatedDate=map(foramatetext,mytext)
for date in myforamatedDate:
    print(date)

#   use lambda functoin
for name in list(map(lambda text : f"- {text} -",mytext)):
    print (name)

#       filter function
#   filter take function + iterator
#   filter run a function on every element 
#   filter out all elements for which the function return true
#   filter return a boolean value 
#   the function can be pre-defiend function or lambda function
print ("#"*50)
def checkevennumber(num):
    if num%2==0 :
        return num

mynumber=range(0,13)
res=filter(checkevennumber,mynumber)
for number in res:
   print(number)

print ("#"*50)
def checkname(name):
    return name.startswith("O")

mylis=["Mohamed","Osama","Ahmed","OOOOOO"]
ress=filter(checkname,mylis)
for name in ress:
    print (name)

print ("#"*50)



mylis=["Mohamed","Osama","Ahmed","OOOOOO","Mahmoud","Magdey"]
ress=filter( lambda name: name.startswith("M")  ,mylis)
for name in ress:
    print (name)

print ("#"*50)

#       reduce function
#   reduce take function + iterator
#   reduce run a function on frist and second element and give result  
#   then run a function on result and third element and give resultt  
#   then run a function on resultt and fourth element and give resulttt and so on  
#   till one element is left and this is the final result of the reduce 
#   the function can be pre-defiend function or lambda function

from functools import reduce # like libraray

def sumall(num1,num2):
    return num1+num2

myli=[1,2,3,4,5,6] # (((((1+2)+3)+4)+5)+6)=21

result = reduce(sumall,myli)
print (result)

print ("#"*50)

names=["Mohamed","hany","Mohamed"]
re=reduce( lambda name1,name2 : name1+ " " +name2 ,names)
print (re)


