# Walrus Operator
# data = [1,2,3,4,5,6]
# if n:= len(data) > 5:
#     print(f"List has {n} items")

# Ternary Operator
# age = 18
# status = "Not an adult" if age <= 18 else "adult"
# print(status)

#Unpacking
# a, *b, c = [1,2,3,4,5,6]
# print(a,b,c)

#
# import threading
# def print_numbers():
#     for i in range(1,6):
#         print(i)
#
# def print_letters():
#     for letter in "abcde":
#         print(letter)
# thread1 = threading.Timer(1,print_numbers)
# thread2 = threading.Thread(target=print_letters)
#
# thread1.start()
# print(thread1.name)
# thread2.start()
# print(thread2.name)
# thread1.join()
# thread2.join()

# import threading
#
# def greet(name,times):
#     for i in range(times):
#         print(f"Hello, {name}")
# thread = threading.Thread(target=greet, args =("Alice",3))
# thread.start()
# thread.join()














