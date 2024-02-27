#   Debugging Functions Calls
# create the decorator to print the function name and args avary time function get called 

# Decorator function 
def debug(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    
    return wrapper
    



def greet(name,greeting="Hello"):
    print(f"{greeting} , {name}")
    


greet("Yogesh","Hey😎")



# Very Basic Decorator

# def debug(func):
#     def wrapper():
#         return func()
#     return wrapper


# @debug
# def hello():
#    print("Hello")