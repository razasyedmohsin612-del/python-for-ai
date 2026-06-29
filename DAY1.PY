from functools import wraps
def decorator1(func):
        @wraps(func)

        def wrapper(*args,**kwargs):
            print("decorator 1 start")
            result = func(*args,**kwargs)
            print("decorator 1 end")
            return result
        return wrapper
   
def decorator2(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print("decorator 2 start")
            result = func(*args,**kwargs)
            print("decorator 2 end")
            return result
        return wrapper
@decorator1
@decorator2
def  add(a,b):
    """this function add two numbers"""
    print(a+b)

add(2,3)

