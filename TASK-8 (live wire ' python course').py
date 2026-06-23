            
#TASK-8
#Q-1
#Write a lambda function to add two numbers.
"""
add=lambda a, b:a+b

x= int(input("Enter first number:"))
y= int(input("Enter second number :"))

print("sum=", add(x,y))

"""

#Q-2
#Write a lambda function to find the square of a number.

"""
square= lambda x: x**2
print(square(5))

"""

#Q-3
#Write a lambda function to find the cube of a number.

"""
cube= lambda x : x**3
print(cube(10))

"""

#Q-4
#Write a lambda function to check whether a number is even or odd.
"""

cheak= lambda x: "Even" if x%2== 0 else "Odd"
print(cheak(5))

"""

#Q-5
#Write a lambda function to find the largest of two numbers.
"""

largest = lambda a,b: a if a>b else b
print(largest(10,20))


"""

#FILTER TASK
#Q-6
#Filter even numbers from a list.
"""
numbers = [1,2,3,4,5,6,7,8,9,10]
even = list( filter(lambda x : x%2==0,numbers))
print(even)
"""

#Q-7
#Filter odd numbers from a list.

"""
numbers = [1,2,3,4,5,6,7,8,9,10]
odd = list(filter(lambda x : x%2!=0, numbers))
print(odd)

"""
#Q-8
#Filter numbers greater than 10.
"""
numbers=[11,13,15,5,6,7,]
greater = list(filter(lambda x : x > 10 , numbers))
print(greater)
"""

#Q-9
#Filter positive numbers from a list.
"""
numbers = [-5, 3, -2, 7, 0, 10, -1]

positive = list(filter(lambda x: x > 0, numbers))

print(positive)

"""

#Q-10
#Filter numbers divisible by 5.
"""
number- [3,4,5,20,30]
divisible= list(filter(lambda x:x%5==0, numbers))
print(divisible)

"""
#MAP TASK
#Q-11
#Use map() to find squares of a list of numbers.
"""
numbers = [1,2,3,4,5]
squares= list(map(lambda x: x**2, numbers))
print(squares)

"""

#Q-12
#Use map() to double all numbers in a list.
"""
numbers = [1, 2, 3, 4, 5]
double = list(map(lambda x: x * 2, numbers))
print(double)

"""

#Q-13
#Use map() to add 5 to each element in a list.
"""
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x + 5, numbers))
print(result)
"""

#q-14
#Use map() to find cubes of numbers in a list.
"""
numbers = [1, 2, 3, 4, 5]
cubes = list(map(lambda x: x ** 3, numbers))
print(cubes)

"""

#q-15
#Use map() to convert numbers into strings.
"""
numbers = [1, 2, 3, 4, 5]
strings = list(map(lambda x: str(x), numbers))
print(strings)
"""

# Combined Map + Filter Tasks 
#q-16
#Filter even numbers and find their squares.
"""numbers = [1, 2, 3, 4, 5, 6]

result = list(map(lambda x: x ** 2,
                  filter(lambda x: x % 2 == 0, numbers)))

print(result)
 
"""

#q-17
#Filter odd numbers and double them.
"""
numbers = [1, 2, 3, 4, 5, 6]
result = list(map(lambda x: x * 2,
                  filter(lambda x: x % 2 != 0, numbers)))
print(result)

"""


#q-19
#Filter numbers greater than 5 and find their cubes.
numbers = [2, 4, 6, 8, 10]

result = list(map(lambda x: x ** 3,
                  filter(lambda x: x > 5, numbers)))

print(result)
