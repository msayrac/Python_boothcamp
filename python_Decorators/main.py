
# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Running the {func.__name__}")
#         result = func(*args,**kwargs)
#         print(f"Exiting the {func.__name__}")
#         return result
#     return wrapper
#
# @log_decorator
# def add(x,y):
#     z = x+y
#     print(z)
#     return z
#
# @log_decorator
# def substract(x,y):
#     z = x - y
#     print(z)
#     return z
#
# print(add(1,8))
# print(substract(10,5))

def capital_decator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs).upper()
        return result
    return wrapper

@capital_decator
def say_hello(x):
    return x

print(say_hello("Hello"))









