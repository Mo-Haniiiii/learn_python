#           Generator
# is a normal function but use "yield" keyword instead of return
# it support iteration and return a generator iterator  by using "yield" keyword
# can have one or more "yield"
# by using next() it resume from where it called "yield" not from begining 
# when called , itsnot start automatically , its only give you the control

def mygenerator():

    yield 1
    yield 2
    yield 3
    yield 4

print (mygenerator())

mygen=mygenerator()
print (next(mygen))
print ("hello")
print (next(mygen))
print (next(mygen))
print (next(mygen))
print ("#"*50)

for num in mygenerator() :
    print (num,end=" ")












