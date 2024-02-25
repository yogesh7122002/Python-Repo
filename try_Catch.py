# file = open("abc.txt","w")

# try:
#     file.write("Adding the Data into the File")
# finally:
#     file.close()
    
    
with open("abc.txt","w") as file:
    file.write("Hey Yogesh Adding data into this file")
    