#replace Pakistan With India
word  = "Pakistan"
replace_word = "Chutiya"
with open("FH/sample.txt","r") as f:
    content = f.read()
print(content)
newCOntent = content.replace(word,replace_word)
print("\n\n")
print(newCOntent)
with open("sample.txt","w") as f:
    f.write(newCOntent)
    
   
    