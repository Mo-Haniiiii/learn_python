#           Boolean
#   true                false
#   you need to know if your code is true or false
#       true value
print (bool(100))
print (bool(100.87))
print (bool("mohamed"))
print (bool(True))
print (bool([1,2,3,4]))

print ("="*50)

#       flase value
print (bool(0))
print (bool(""))
print (bool(''))
print (bool([]))
print (bool(False))
print (bool(()))
print (bool({}))
print (bool(None))

print ("="*50) 

#           Boolean operators
#      and          or          not         
name="mohamed"
age =19
print ( name=="mohamed" and age==19)
print ( name=="mohamed" and age==10)

print ( name=="mohamed" or age==19)
print ( name=="ahmed" or age==10)

print (age==19)
print (not age==19)    

#           Assignment operators
# =     +=      -=      *=      /=      **=     %=      //=

#           Comparison Operators
# ==    !=      <=      >=      <       >


#           Date Type Conversion

# str we can change the int or float to string
# int we can change the string or float to int
# float we can change the string or int to float
#           tuple 

#s="mohamed"
#lis=[1,2,3,4]
#set={12,4,15,2}
#dic={"one":1,"two":2,"three":3}
#print(tuple(s))
#print(tuple(lis))
#print(tuple(set))
#print(tuple(dic))

#              list 
#s="mohamed"
#tup=(1,2,3,4)
#set={12,4,15,2}
#dic={"one":1,"two":2,"three":3}
#print(list(s))
#print(list(tup))
#print(list(set))
#print(list(dic))

#               set
#s="mohamed"
#tup=(1,2,3,4)
#lis=[12,4,15,2]
#dic={"one":1,"two":2,"three":3}
#print(set(s))
#print(set(tup))
#print(set(lis))
#print(set(dic))

#               dict

#tup=((1,2),(3,4))
#lis=[[1,2],[3,4]]

#print(list(tup))
#print(dict(lis))