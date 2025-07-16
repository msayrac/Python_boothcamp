
# my_list = [1,2,3,4,5]

# new_list = []
# for num in my_list:
#     new_list.append(num)
# print(new_list)


# expression for item in iterable if condiiton
# my_list = [1,2,3,4,5]
# new_list =[num*num for num in my_list if num%2==0]
# print(new_list)
#
#
# even_list = ["even" if num % 2 ==0 else "odd" for num in my_list]
# print(even_list)

# words = ["apple","banana","chery","dog","elephant"]
# long_words = [x.capitalize() for x in words]
# print(long_words)
#
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# flatten = [num for row in matrix for num in row]
# print(flatten)

# list1 = [1,2,3]
# list2 = [4,5,6]
#
# result = [a*b for a,b in zip(list1, list2)]
# print(result)

# enumerate

# fruits = ['apple', 'banana', 'orange']
# counter = 0
# for fruit in fruits:
#     print(counter, fruit)
#     counter += 1
#
# for index, fruit in enumerate(fruits,start=1):
#     print(index, fruit)
#     print(index)


# colors = ("red", "green", "blue")
#
# for index, color in enumerate(colors,start=1):
#     print(index, color)

numbers = [10,20,30,40]
squared = [x**2 if i%2 == 0 else x for i, x in enumerate(numbers)]
print(squared)
















