# how much time is this function taking for execute
import time

# DEcorators in python


def timer(func):
    def wrapper(*args,**kwargs):
        
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start}")
        return result
    
    return wrapper


#this is The Notation used for the decorator in python 

@timer
def example_function(n):
    time.sleep(n)
    
example_function(3)
