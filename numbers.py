# integer = int
print (type (10))
print (type (110))
print (type (-10))
print (type (0))
print (type (-110))

# float
print (type (10.9))
print (type (110.12))
print (type (-10.3421))
print (type (0.28))
print (type (-110.129))

# complex number 
print (type (5+6j)) 
#   real number         imaginary
#       5                   6j
complexnumber=5+6j
print (f"the real number is : {complexnumber.real}")
print ("the real number is : {}".format(complexnumber.imag))

# we can convert the int to float and complex and string
# we can convert the float to int and complex and string
# we cannot convert the complex to any date type
intt=10
print (float(intt))
print (complex(intt)) 
print (str(intt))

flloat=10.5
print (int(flloat))
print (complex(flloat))

#Exponent => power 
print (2 ** 2) # (2*2)
print (5 ** 4) # (5*5*5*5)







