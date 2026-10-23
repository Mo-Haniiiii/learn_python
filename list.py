
#           list 
# list iteams are Enclosed is []
# list can contain many date type
# list iteams can change
mylist= [1,2.5,"mohamed",True,[1,2,3]]
# list iteams are ordered in index   zero based 
print (mylist[0])  #1
print (mylist[-1]) #[1,2,3]
print (mylist)
print (mylist[2:4])
print (mylist[4][0])
# list methods

#   append() to add iteam to the list
#   extend()
a=[1,2,3,4]
b=["a","b","c"]
a.extend(b)
print (a)
#   remove(iteam) to remove the iteam from the list  
#   sort (reverse) to sort the list from small to big   =>iteams are same date type
#   sort (reverse=True) to sort the list from big to small =>iteams are same date type
#   reverse() to reverse the list 
#   clear() to remove all iteams
#   copy()  to copy iteams from list to anthor 
#   count() to know how many the number repeted
#   index() to know the index of element
#   insert(index, iteam) insert iteam before index
#   pop(index) to return the iteam in index 