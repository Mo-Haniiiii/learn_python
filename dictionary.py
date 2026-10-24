#                 Dictionary
#     dict iteams are Enclosed is {}
#     dict iteam is key and value  
#     dict key (string ,number,tuble),value any date type
#     dict iteam is unique
#     dict not ordered , not indexed and not slicing
# 
#        
mydic={
"one":1,"two":2,"three":3
}
print (mydic)
print (mydic["one"])
print (mydic.get("one"))
print (mydic.keys())
print (mydic.values())

#   two dimensional dict
language={
    1:{
        "name":"c++",
        "progress":90
    },
    2:{
        "name":"python",
        "progress":80
    },
    3:{
        "name":"css",
        "progress":50
    }
}
print (language)
print (language[1]["name"])

#           dict method
#   length() 
#   clear() to remove all iteams
#   update() to add element to the dict
#   copy()  to copy iteams from dict to anthor 
print (len(language))
print (len(language[1]))

#   setdefault()
user={
    "name":"mohamed"
}
print (user)
print (user.setdefault("age",19))
print (user)

#   popiteam()
user1={
    "name":"mohamed"
}
user1.update({"age":19})
print (user1.popitem())

#   fromkeys()
mykeys=("one","two","three")
value="x"
print (dict.fromkeys(mykeys,value))



