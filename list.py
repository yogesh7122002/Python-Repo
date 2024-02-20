names =["Tushar","Yogesh","OM"]
# print(names)

# print(names[1:3])
# print(names[1:1]) #this will print nothing

# print(names[])
# names[1:1]=["test","Test"] #this much content is get inserted into the 1st posting to end of 1st postion
# print(names)


# names[1:1]=[] #this will insert the emty content into those positions
# print(names) #this will remove the test and Test COntent from The between the list

# traversing through the tea

# for name in names:
#     print(name, end=" ")

# if "OM" in names :
#     print("Present")
# else :
#     print("No Present")
 
 
# names.append("Sai")
# names.append("OM")

# print(names)

# print(names.pop())



#for Removing the elements from the list remove inbuild method
# print(names)
# names.remove("OM")
# print(names)
# names.append("OM")
# print(names)


#insert at the specific indec
# names.insert(1,"Sai")
# print(names)


# You can create the copy with the same refrance and Differance refrance 

# names_copy = names #this will be heaving the same memory refrance 
# names_copy1= names.copy() # this will be heaving the different memory access

# copy() method is used to created the different refranced copy

# name_cpy = names.copy()
# print(name_cpy)

# names_copy = names #creating the copy with the same refrance 
# print(names)
# #appending The new element to the copy but due to heaving the same refrance in this will get appended to the names also

# names_copy.append("Sai")

# print(names)



#complex list syntax
squared_nums = [x**2 for x in range(10)] #this will print adding all the squares till the 9 into the list
print(squared_nums)


