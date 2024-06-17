

def genrate_table(n):
    
    tables =""
    for i in range(1,11):
        tables += f"{i} X {n}={i*n}\n"
    with open(f"Tables/table_{n}","w") as f:
        f.write(tables)
        
    
    # pass



for i in range(1,11):
    genrate_table(i)