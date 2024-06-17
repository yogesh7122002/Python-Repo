word="Think"

with open("abc.txt","r") as f:
    content = f.read()
    if(word in content):
        print("Word Think is present in think")
    else:
        print("Word Think is Not present in think")
