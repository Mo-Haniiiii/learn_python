myString1 = "Mohamed hany" # doubel quote
myString2= 'Mohamed hany' # singel quote
print (myString1)
print (myString2)

# indexing (Access singel iteam)
# string is array of char
# positive index get the char from left  zero based
st= "mohamed hany"
print (st[0])# =>m
print (st[8])# =>h

# negitive index get the char from rigth 1 based
print (st[-1])# => y
print(st[-7])# => e

# slicing (Access mulitple sequence iteams)
print (st[4:7])#   med
print (st[9:11])#    an 
print (st[:6])# if  start is not here will start from 0 &&End not include means (end -1) (mohame)
print (st[2:])# if  End is not here will go to end   (hamed hany)
print (st[:]) # full date (mohamed hany)

#    string method
st = "i love python"
myString = "        i love python        "
print (len(st))  # len(value) = length 
# strip()    rstrip()    lstrip()    to remove the spaces
# strip("#")    rstrip("#")    lstrip("#")    to remove the #
print (myString.strip())
print ("####i love python####".strip("#"))
#   titel() make the frist char in string is capital and the char after num
n= "mohamed hany"
print (n.title())# Mohamed Hany

#   capitalize() make the frist char in string is capital
n= "mohamed hany"
print (n.capitalize())# Mohamed hany

# uper() => make all chars capital
print (n.upper())

# lower() => make all chars small
print (n.lower())

# split()    rspilt()
s ="i love python and cpp"
print (s.split()) # ['i', 'love', 'python', 'and', 'cpp']
a ="i love python and cpp"
print (s.split(" ",2)) # ['i', 'love', 'python and cpp']

#   center()
b= " mohamed hany "
print (b.center(20,"-"))

#   count()
c =" i love  python and php becouse its easy " 
print (c.count("php"))

# swapcase()        change the capital char to small w el 3aks
d = "heLLO wOLlD"
e = "MOhaMed hAnY"
print (d.swapcase())
print (e.swapcase())

# startswith()       show if the string start with the char return True else False
f= "I love money"
print (f.startswith("I"))   # True

# endswith()       show if the string end with the char return True else False
j ="I love money"
print (j.endswith("y"))   # True

#   index(substring, start,end)
aa = "i love money"
print (aa.index("m")) # return the index 
print(aa.index("m",0,10)) # return the index 

#   find(substring, start,end)
aa = "i love money"
print (aa.index("m")) # return the index 
print(aa.index("m",0,10)) # return the index 

#   rjust(width,full char)     ljust(width,full char)
bb = "mohamed"
print (bb.rjust(10))
print (bb.rjust(13,"#"))# full char

cc = "mohamed"
print (cc.ljust(10))
print (cc.ljust(13,"#"))# full char

#ٍ   replace(old value , new value,count)
dd="hello one two three one one"
print (dd.replace("one","1",3))

#           string formatting

name1="mohamed"
age = 19
rank= 10
#print("my name is : "+name1+" "+"my age is : "+age)     #type error
print("my name is : %s my age is : %d my rank is : %f" % (name1,age,rank))
#   repalcement
# %s => string  %d =>number     %f =>float
print("my name is : {} my age is : {} my rank is : {}".format(name1,age,rank))
print(f"my name is : {name1} my age is : {age} my rank is : {rank}")
