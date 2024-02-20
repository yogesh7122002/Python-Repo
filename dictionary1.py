#dictionary stores the values into the key value and pair

names = {"sai":"Coder","om":"AWS Pro","Tushar":"Master In Js","Yogesh":"Noob at Everything"}
# print(names)
# print(names["Yogesh"])
# print(names["om"])
# print(names["sai"])
# print(names["Tushar"])


# print(names.get("Tushar"))
# print(names.get("Tushar"))
# names["Tushar"]="Washim"
# print(names.get("Tushar"))


# for name in names:
#     print(name," : ",names[name])


# traverse over the dictionary with the keys and values


# for keys,values in names.items():
#     print(keys,":", values)



# Insert new Element into The dictionary

# names["Kishor"] ="New Roommate" #Syntax

# for keys,values in names.items():
#     print(keys,":", values)


# POP methos is there but you have to provide the key for The Option
# names["aman"] ="Pro Boy"; #Adding The New entry into the dictionary
# for key,value in names.items():
#     print(key,":",value)
    
# print(names.pop("aman"))

# print("\n\nRemoved aman \n\n")

# for key,value in names.items():
#     print(key,":",value)
    
# another method is there to remove the the last item in the dictionary

# names["aman"]= "He Boy"
# print(names.popitem()) #this will display The removed item from the list


# Another way to delete the 
# names["aman"]= "He Boy"
# print(names)
# del names["aman"] #this will delete the refrance from the memory 
# print(names)


# now we are going to see the dictionary inside the dictionary
# cse ={"a_div":{"karan":"coder","sai":"roomate","om":"aws Master","vaishnavi":"Friend"},"b_div":{"yogesh":"Self","tushar":"Friend","amogh":"Gand Dost"},"c_div":{"vinay":"Company mate","saira":"Company mate"}}



# # for key,value in cse.items():
# #     print(key,":",value)


# print(cse["a_div"]["karan"])
# print(cse["a_div"]["vaishnavi"])
# print(cse["b_div"]["yogesh"])



# so lets print the list with the number and its square
# squre_key = {x:x**2 for x in range(21)}
# print(squre_key)


# creating dictionary from arrays
keys = ["yogesh","sai","Tusahr"]
default_value ="Good Boys"

# new_Dict = dict.fromkeys(keys,default_value)
print(dict.fromkeys(keys,default_value))
print(dict.fromkeys(keys,keys))
