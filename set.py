#           set
#   set iteams are Enclosed is {}
#   set not ordered , not indexed and not slicing
#   set date type (string,number,tuble) no list or dict
#   set iteam is unique
myset={1,"mohamed",2,2,"mohamed",1}
print (myset)    

#           set method
#   clear() to remove all iteams
#   union()
a={1,2,3}
b={"one","two","three"}
print (a.union(b))
#   add(one iteam)
#   copy()  to copy iteams from set to anthor 
#   remove(iteam) to remove the iteam from the set  
#   pop() to return the random iteam 
#   diffierence() return the diffierencebetween to sets  set1-set2
#   intersection() eltaqato3
#   issuperset()
c={1,2,3,4}
d={1,2,3}
print (c.issuperset(d))

#   issubset()
aa={1,2,3,4}
bb={1,2,3}
print (c.issuperset(d))# false   all iteam aa not found in bb

#   isdisjoint()
cc={1,2,3,4}
dd={1,2,3}
print(cc.isdisjoint(dd))# false some iteams dd found in cc
