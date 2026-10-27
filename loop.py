#           while loop
#   while condition True :
#       code will run    
a = 1
while a<=5 :
    print(a)
    a+=1
print ("#"*30)
myf=["a","b","c","d","e","f","g","h","i","j"]

b=0
while b<len(myf) :
    print(f"{str(b+1).zfill(2)}# {myf[b]}")
    b +=1
print ("#"*30)

myfav=[]
maxweb=5
#while maxweb>0:
#    iteam=input(" Enter the web name ").strip()
#    myfav.append(iteam)
#    maxweb-=1
#    print (f"web site append & {maxweb} places left")
#    print (myfav)
#else :
#    print (" The list is full ")    
#
#if len(myfav)>0 :
 #   myfav.sort()
 #    i=0
#    print (" The sorted list : ")
#    while i<len(myfav) :
#        print (myfav[i])
#        i+=1
#else :
#    print (" The list is empty ")        

#       forloop
# for iteam in iterable object 
#  Range 
#myRange=Range(1,100)   ->> 1 -> 99
#   for number in myRange 
#   print (number)

listt=[1,2,3,4,5,6]
print (" Even numbers ")
for num in listt:
    if num % 2 == 0 :
        print (num)    
print (" Odd numbers ")
for num in listt:
    if num % 2 != 0 :
        print (num)           
    
name="mohamed"
for letter in name:
    print (letter)

print ("#"*30)

dic={"one":1,"two":2,"three":3,"four":4}
for stri in dic :
    print (f" {stri} is {dic[stri]}")

print ("#"*30)

diic={
"mohamed":{
    "cpp":"90%",
    "python":"60%"
    },
"ahmed":{
    "css":"80%",
    "js":"70%"
    },
"ali":{
"html":"95%",
"python":"50%"        
    }
}
#for name in diic:
 #   print (f" my name is {name} ")
#    for skill in diic:
#        print (f" the skill and progress is {diic[name]} ")
#        break
#else :
#    print (" the loop is done ")

#       Advanced loop
for key , value  in diic.items():
    print (f" My name is {key} The progress is ")
    for key2,value2 in value.items() :
        print (f" {key2}=={value2}")






print ("#"*30)

#   break to stop the block of code

Mynum=[1,2,4,5,8,10,13,15]
for number in Mynum:
    if number==13:
        break
    print (number)    #[1,2,4,5,8,10]

    for number in Mynum:
         print (number)   #[1,2,4,5,8,10,13 ]
         if number==13:
            break

#   continue to skip 

Mynum=[1,2,4,5,8,10,13,15]
for number in Mynum:
    if number==13:
        continue
    print (number)    #[1,2,4,5,8,10,15]

#   pass 

Mynum=[1,2,4,5,8,10,13,15]
for number in Mynum:
    if number==13:
        pass
    print (number)    #[1,2,4,5,8,10,13 ,15]

print ("#"*30)
myskills={
    "cpp":80,
    "python":90,
    "html":50
}
#for skil in myskills:
   # print(f" The skill name is {skil} and the progress is {myskills[skil]}")
#           Advaned loop

for key ,value in myskills.items() :
    print (f" The skill name is {key} and the progress is {value}")



