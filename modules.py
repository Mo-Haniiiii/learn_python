#                   modules 

# module is a file contain a set of funcion
# you can import a module in your app to help you
# you can import multiple modules
# you can creat your own module
# module save your time

#  import main module
import random
print (dir(random)) # to know all functions in module



print ("#"*30)
from random import random ,randint
print (f"print random float number {random()}")
print ("#"*30)
print (f"print random integer number {randint(100,900)}") # lazm range
print ("#"*30)

#import creat

#print (dir(creat))             sayhello - sayHowAreYou
#creat.sayhello("Mohamed")
#creat.sayhello("Ahmed")
#creat.sayhello("Ali")

#creat.sayHowAreYou("Mohamed")
#creat.sayHowAreYou("Ahmed")
#creat.sayHowAreYou("Ali")

import creat as cr

cr.sayhello("Mohamed")
cr.sayhello("Ahmed")
cr.sayhello("Ali")

cr.sayHowAreYou("Mohamed")
cr.sayHowAreYou("Ahmed")
cr.sayHowAreYou("Ali")

from creat import sayhello as ss

ss("Mohamed")

print ("#"*30)

#       date and time  ---->  module

import datetime

print (dir(datetime))
print ("#"*60)
print (dir(datetime.datetime))
print ("#"*60)
# if we want to print the date and time now
print (datetime.datetime.now())
print ("#"*60)
# if we want to print the current year 
print (datetime.datetime.now().year)
# if we want to print the current month
print (datetime.datetime.now().month)
# if we want to print the current day
print (datetime.datetime.now().day)
print ("#"*30)
# if we want to print the start and the end of date
print (datetime.datetime.min)
print (datetime.datetime.max)
print ("#"*30)
# if we want to print the current time
print (datetime.datetime.now().time())
# if we want to print the current time hour
print (datetime.datetime.now().time().hour)
# if we want to print the current time minute
print (datetime.datetime.now().time().minute)
# if we want to print the current time second
print (datetime.datetime.now().time().second)
print ("#"*30)
# if we want to print the start and the end of time
print (datetime.time.min)
print (datetime.time.max)
print ("#"*30)
# if we want to print the specific date
print (datetime.datetime(2007,10,1,20,30,0,0))
print ("#"*30)
# if we want to print how much time did live
mybirthday = datetime.datetime(2007,10,1,20,30,0,0)
datenow=datetime.datetime.now()
print (f" i lived for {datenow-mybirthday} ") 
print (f" i lived for {(datenow-mybirthday).days} days ") # days only
print ("#"*30)
#  formate date and time 
#  strftime("%B")
mybir=datetime.datetime(2007,10,1)
print (mybir)
print (mybir.strftime("%B")) # the month
print (mybir.strftime("%A")) # the day  
print (mybir.strftime("%a")) # the day but mo5tasar
print (mybir.strftime("%b")) # the month but mo5tasar 
print (mybir.strftime("%d")) # the number of day 
print (mybir.strftime("%d / %B / %Y")) # birthday
print ("#"*30)

#       to change th itreable (set,string,tuple,list,dictionary) to iterator
#                       we use the function iter(itreable)
stri="Mohamed"
myiterator=iter(stri)
#print (next(myiterator))
#print (next(myiterator))
#print (next(myiterator))
#print (next(myiterator))
#print (next(myiterator))
#print (next(myiterator))
#print (next(myiterator))

for letter in myiterator:
    print (letter,end=" ")





