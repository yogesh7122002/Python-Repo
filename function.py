# # we are creating the function for calculating the geometric mean
# def gemean(a,b):
#     mean = (a*b)/(a+b)
#     print("the mean of the given numbers is ",round(float(mean),2))
    
    
# a = int(5)
# b = int(6)
# gemean(5,6)


# def calculateGmean(a, b):
#   mean = (a*b)/(a+b)
#   print(round(mean,2))

# def isGreater(a, b):
#   if(a>b):
#     print("First number is greater")
#   else:
#     print("Second number is greater or equal")

# def isLesser(a, b):
#   pass
  

# a = 9
# b = 8
# isGreater(a, b)
# calculateGmean(a, b)
# # gmean1 = (a*b)/(a+b)
# # print(gmean1)
# c = 8
# d = 74
# isGreater(c, d)
# calculateGmean(c, d)
# # gmean2 = (c*d)/(c+d)
# # print(gmean2)


# # Default arguments:

# def name(fname, mname = "Jhon", lname = "Whatson"):
#     print("Hello,", fname, mname, lname)

# name("Sam")

# # Keyword arguments:
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name(mname = "Peter", lname = "Wesker", fname = "Jade")


# # Required arguments:
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name("Peter", "Quill")

# Variable-length arguments
def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("Yogesh", "Balu", "Deshmane")


# #Keyword Arbitrary Arguments

# def name(**name):
#     print("Hello,", name["fname"], name["mname"], name["lname"])

# name(mname = "Buchanan", lname = "Barnes", fname = "James")