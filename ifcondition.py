#           if condition
#   if condition :   
#       print ()

uname="mohamed"
ucountry="Egypt"
cname="python course"
cprice=100
age=18
uage=17
if ucountry=="Egypt" or ucountry == "France" :
    if uage < age :
        print (f" Hello {uname} becouse you are from {ucountry} And you are under age ")
        print (f" The course name is {cname} and the price is {cprice-70} ")
    else:
        print (f" Hello {uname} becouse you are from {ucountry} ")
        print (f" The course name is {cname} and the price is {cprice-50} ")

elif ucountry=="KSA" :
    print (f" Hello {uname} becouse you are from {ucountry} ")
    print (f" The course name is {cname} and the price is {cprice-40} ")

else :
    print (f" Hello {uname} becouse you are from {ucountry} ")
    print (f" The course name is {cname} and the price is {cprice-20} ")

movierate=18
agee=18

print (" the movie is not good for you " if movierate>agee else " the movie is good for you ")

#               membership operations
#             in                     not in

lis=[1,2,3]
print (1 in lis) # True
print (4 in lis) # False
print (4 not in lis )# True

print ("#"*30)

frindes=["mohamed","ahmed","ali"]
print ("mohamed" in frindes) # True
print ("galal" in frindes) # False
print ("galal" not in frindes) # true

countriesone=["Egypt","Ksa","Qatar"]
countriesonedis=80
countriestwo=["Usa","itali"]
countriestwodis=50
#mycountry=input("Enter your country ")
#if mycountry in countriesone :
 #   print (f" You have a discount = {countriesonedis}")
#elif mycountry in countriestwo : 
#    print (f" You have a discount = {countriestwodis}")
#else:
 #   print (" You have not a discount ")
print ("#"*40)


adminlis=["ahmed","osama","mahmoud","sara","rahma","mohamed"]

name=input(" Please enter your name : ").strip()

if name in adminlis :

    print (f" Hello {name} welcome back ")

    option=input(" delet or update your name ? ").strip().capitalize()

    if option=="Update" :

        thenewname=input(" Enter the new name : ").strip()

        adminlis.index(name)=thenewname

        print (" name updated : "+ adminlis)
    elif option=="Delet" : 

        adminlis.remove(name)

        print (" name deleted : "+ adminlis)
    else :
        print (" wrong opiton ")
else :    
    status=input(" Not admin do you want to be admin ? ")
    if status=="Yes" or status=="Y" or status == "yes" :
        namee=input(" Enter the name to add in the list : ").strip()
        adminlis.append(namee)
    else:
        print(" you are not added ")        