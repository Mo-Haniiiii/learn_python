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


