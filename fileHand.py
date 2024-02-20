
# Performing The read Operation on the file

# f = open("abc.txt","r")
# data = f.read()
# print(data)
# print(type(data))

# This Process will override the data in the file 
# means older data get removed with the new data 

# f = open("abc.txt","w")
# f.write("\nThis Is new Line I'm Adding into The File So Please note this one")
# f.close()


# For Displyaing The data from the file

# f = open("abc.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()


# Performing The write Operation on the file







# /workspaces/Python-Repo/abc.txt


# For Appeding The New data into the file you have to open the file in 'a' Mode 

f = open("abc.txt","a")

f.write("\nI'm appeding the new data to the file ")
f.close()


f = open("abc.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()