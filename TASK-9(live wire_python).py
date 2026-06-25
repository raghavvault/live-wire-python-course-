# ==============================
# 1. MATH MODULE TASKS
# ==============================

import math

print("===== MATH MODULE =====")

# Task 1
print("Square root of 144 =", math.sqrt(144))
print("5^3 =", math.pow(5, 3))
print("Factorial of 6 =", math.factorial(6))
"""
# Task 2
print("Ceil of 5.2 =", math.ceil(5.2))
print("Floor of 5.8 =", math.floor(5.8))
print("GCD of 24 and 36 =", math.gcd(24, 36))

# Task 3 - Calculator
print("\nCalculator")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+,-,*,/,^): ")

if op == "+":
    print("Result =", a + b)
elif op == "-":
    print("Result =", a - b)
elif op == "*":
    print("Result =", a * b)
elif op == "/":
    print("Result =", a / b)
elif op == "^":
    print("Result =", math.pow(a, b))
else:
    print("Invalid operator")


# ==============================
# 2. DATETIME MODULE TASKS
# ==============================

from datetime import datetime

print("\n===== DATETIME MODULE =====")

now = datetime.now()

# Task 1
print("Current Date:", now.date())
print("Current Time:", now.time())
print("Current Year:", now.year)

# Task 2 - Age
dob = datetime(2008, 6, 15)     # Change to your DOB
age = now.year - dob.year

if (now.month, now.day) < (dob.month, dob.day):
    age -= 1

print("Age:", age)

# Task 3
print("Today's Date (DD-MM-YYYY):", now.strftime("%d-%m-%Y"))


# ==============================
# 3. DATE MODULE TASKS
# ==============================

from datetime import date

print("\n===== DATE MODULE =====")

# Task 1
birthday = date(2008, 6, 15)      # Change to your DOB
print("Birthday:", birthday)

# Task 2
today = date.today()
difference = today - birthday
print("Difference:", difference)

# Task 3
print("Day:", birthday.day)
print("Month:", birthday.month)
print("Year:", birthday.year)


# ==============================
# 4. CALENDAR MODULE TASKS
# ==============================

import calendar

print("\n===== CALENDAR MODULE =====")

# Task 1
print(calendar.month(today.year, today.month))

# Task 2
print(calendar.calendar(2026))

# Task 3
print("2024 Leap Year?", calendar.isleap(2024))
print("2025 Leap Year?", calendar.isleap(2025))
print("2028 Leap Year?", calendar.isleap(2028))

# Task 4
weekday = calendar.day_name[birthday.weekday()]
print("Birthday falls on:", weekday)


# ==============================
# 5. PYWHATKIT TASKS
# ==============================

import pywhatkit

print("\n===== PYWHATKIT MODULE =====")

# Task 1
# Replace with your own phone number
# pywhatkit.sendwhatmsg("+91XXXXXXXXXX", "Hello from Python!", 18, 30)

# Task 2
pywhatkit.search("Python Programming")

# Task 3
pywhatkit.playonyt("Python Tutorial")

# Task 4
pywhatkit.text_to_handwriting("Python Programming is Fun!", "handwriting.png")
print("Handwriting image saved as handwriting.png")


# ==============================
# 6. RANDOM MODULE TASKS
# ==============================

import random

print("\n===== RANDOM MODULE =====")

# Task 1
print("Random Number:", random.randint(1, 100))

# Task 2
otp = random.randint(100000, 999999)
print("OTP:", otp)

# Task 3
dice = random.randint(1, 6)
print("Dice:", dice)

# Task 4 - Rock Paper Scissors
choices = ["Rock", "Paper", "Scissors"]

user = input("Enter Rock, Paper or Scissors: ").capitalize()
computer = random.choice(choices)

print("Computer:", computer)

if user == computer:
    print("Match Draw")
elif (user == "Rock" and computer == "Scissors") or \
     (user == "Paper" and computer == "Rock") or \
     (user == "Scissors" and computer == "Paper"):
    print("You Win!")
else:
    print("Computer Wins!")


# ==============================
# 7. NUMPY MODULE TASKS
# ==============================

import numpy as np

print("\n===== NUMPY MODULE =====")

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
"""
