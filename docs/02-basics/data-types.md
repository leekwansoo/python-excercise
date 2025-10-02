# Python Data Types - Understanding Your Data 📊

## Introduction

Data types are the foundation of all programming. They tell Python what kind of data you're working with and what operations you can perform on that data. Understanding data types is crucial for writing effective Python programs.

Think of data types as different containers for different kinds of information - just like you use different containers in real life for different purposes!

## 🎯 Learning Objectives

After completing this lesson, you will:
- Understand Python's built-in data types
- Know when to use each data type
- Convert between different data types
- Avoid common data type mistakes
- Write more efficient and bug-free code

---

## 🧰 Python's Built-in Data Types

Python has several built-in data types, each designed for specific purposes:

| Category | Data Type | Description | Example |
|----------|-----------|-------------|---------|
| **Text** | `str` | Strings (text) | `"Hello World"` |
| **Numeric** | `int` | Integers (whole numbers) | `42` |
| **Numeric** | `float` | Decimal numbers | `3.14159` |
| **Numeric** | `complex` | Complex numbers | `3+4j` |
| **Boolean** | `bool` | True/False values | `True`, `False` |
| **Sequence** | `list` | Ordered, changeable collections | `[1, 2, 3]` |
| **Sequence** | `tuple` | Ordered, unchangeable collections | `(1, 2, 3)` |
| **Sequence** | `range` | Sequence of numbers | `range(5)` |
| **Mapping** | `dict` | Key-value pairs | `{"name": "John"}` |
| **Set** | `set` | Unordered, unique collections | `{1, 2, 3}` |

---

## 📝 Text Data: Strings (str)

Strings represent text data and are one of the most commonly used data types.

### Creating Strings:
```python
# Different ways to create strings
name = "Alice"
message = 'Hello World'
long_text = """This is a 
multi-line string"""

# Empty string
empty = ""
```

### String Operations:
```python
first_name = "John"
last_name = "Doe"

# String concatenation (joining)
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe

# String formatting
age = 25
introduction = f"My name is {full_name} and I am {age} years old"
print(introduction)
```

### Useful String Methods:
```python
text = "Python Programming"

print(text.upper())        # PYTHON PROGRAMMING
print(text.lower())        # python programming  
print(text.replace("Python", "Java"))  # Java Programming
print(len(text))           # 18 (length of string)
print(text.split())        # ['Python', 'Programming']
```

---

## 🔢 Numeric Data Types

### Integers (int)
Whole numbers without decimal points:

```python
# Positive and negative integers
positive = 42
negative = -17
zero = 0

# Large integers (Python handles big numbers automatically)
big_number = 123456789012345678901234567890

# Different number bases
binary = 0b1010      # Binary (base 2) = 10 in decimal
octal = 0o12         # Octal (base 8) = 10 in decimal  
hexadecimal = 0xA    # Hexadecimal (base 16) = 10 in decimal
```

### Floating Point Numbers (float)
Numbers with decimal points:

```python
# Basic floats
pi = 3.14159
temperature = -15.5
percentage = 0.85

# Scientific notation
speed_of_light = 2.998e8  # 2.998 × 10^8
small_number = 1.23e-4   # 1.23 × 10^-4
```

### Arithmetic Operations:
```python
# Basic operations
print(10 + 3)    # Addition: 13
print(10 - 3)    # Subtraction: 7
print(10 * 3)    # Multiplication: 30
print(10 / 3)    # Division: 3.3333...
print(10 // 3)   # Floor division: 3
print(10 % 3)    # Modulus (remainder): 1
print(10 ** 3)   # Exponentiation: 1000
```

---

## ✅ Boolean Data: True or False (bool)

Booleans represent truth values and are essential for decision-making in programs:

```python
# Boolean values
is_sunny = True
is_raining = False

# Comparison operations return booleans
print(5 > 3)     # True
print(10 == 10)  # True
print(7 != 7)    # False

# Logical operations
print(True and False)  # False
print(True or False)   # True
print(not True)        # False
```

### Common Boolean Expressions:
```python
age = 18
has_license = True

# Combining conditions
can_drive = age >= 18 and has_license
print(f"Can drive: {can_drive}")  # True

# Using booleans in conditions
if can_drive:
    print("You can drive!")
else:
    print("You cannot drive yet.")
```

---

## 📋 Sequence Data Types

### Lists (list) - Ordered and Changeable
```python
# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True, 3.14]

# List operations
fruits.append("orange")      # Add item
print(fruits[0])            # Access first item: apple
fruits[1] = "blueberry"     # Change item
print(len(fruits))          # Get length
```

### Tuples (tuple) - Ordered but Unchangeable
```python
# Creating tuples
coordinates = (10, 20)
rgb_color = (255, 128, 0)
single_item = (42,)  # Note the comma for single-item tuple

# Tuple operations (limited because they're immutable)
x, y = coordinates          # Unpacking
print(f"X: {x}, Y: {y}")   # X: 10, Y: 20
```

---

## 🗂️ Mapping Data: Dictionaries (dict)

Dictionaries store data in key-value pairs:

```python
# Creating dictionaries
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "courses": ["Python", "Math", "Physics"]
}

# Dictionary operations
print(student["name"])              # Access value: Alice
student["age"] = 21                 # Update value
student["email"] = "alice@edu.com"  # Add new key-value pair

# Useful dictionary methods
print(student.keys())               # Get all keys
print(student.values())             # Get all values
print(student.get("phone", "N/A"))  # Get with default value
```

---

## 🔍 Checking and Converting Data Types

### Checking Data Types:
```python
# Using type() function
print(type(42))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("hello"))     # <class 'str'>
print(type(True))        # <class 'bool'>

# Using isinstance() function (preferred)
age = 25
if isinstance(age, int):
    print("Age is an integer")
```

### Converting Between Types:
```python
# String to number conversion
text_number = "42"
number = int(text_number)        # Convert to integer
decimal = float(text_number)     # Convert to float

# Number to string conversion
age = 25
age_text = str(age)              # Convert to string

# Boolean conversions
print(bool(1))          # True
print(bool(0))          # False
print(bool(""))         # False (empty string)
print(bool("hello"))    # True (non-empty string)
```

---

## 🎯 Practical Examples

### Example 1: User Profile System
```python
# User profile using different data types
user_profile = {
    "username": "pythonlover",           # string
    "user_id": 12345,                    # integer
    "email": "user@example.com",         # string
    "account_balance": 1250.75,          # float
    "is_premium": True,                  # boolean
    "favorite_languages": ["Python", "JavaScript", "Go"],  # list
    "last_login": (2023, 10, 15),       # tuple (year, month, day)
}

# Working with the profile
print(f"Welcome, {user_profile['username']}!")
if user_profile["is_premium"]:
    print("You have premium access!")

# Add new favorite language
user_profile["favorite_languages"].append("Rust")
```

### Example 2: Shopping Cart Calculator
```python
# Shopping cart with mixed data types
shopping_cart = [
    {"item": "laptop", "price": 999.99, "quantity": 1},
    {"item": "mouse", "price": 25.50, "quantity": 2},
    {"item": "keyboard", "price": 89.99, "quantity": 1}
]

# Calculate total
total = 0.0
for item in shopping_cart:
    item_total = item["price"] * item["quantity"]
    total += item_total
    print(f"{item['item']}: ${item_total:.2f}")

print(f"Total: ${total:.2f}")
```

---

## 🚀 Interactive Practice

Ready to practice with Python data types? Click below to open an interactive environment:

[![Practice Data Types](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/leekwansoo/python-excercise/main?labpath=_2DataTypes.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/leekwansoo/python-excercise/blob/main/_2DataTypes.ipynb)

**In the interactive notebook, you'll:**
- Experiment with all data types
- Practice type conversion
- Build real-world examples
- Learn to debug type-related errors

---

## ⚠️ Common Data Type Pitfalls

### 1. String vs Number Confusion
```python
# Problem
age_input = "25"  # This is a string!
next_year = age_input + 1  # Error! Can't add number to string

# Solution
age = int(age_input)  # Convert to integer first
next_year = age + 1   # Now this works
```

### 2. Integer Division vs Float Division
```python
# In Python 3
print(10 / 3)   # 3.3333... (float division)
print(10 // 3)  # 3 (integer/floor division)
```

### 3. Mutable vs Immutable Confusion
```python
# Lists are mutable (can be changed)
my_list = [1, 2, 3]
my_list[0] = 99  # This works

# Tuples are immutable (cannot be changed)
my_tuple = (1, 2, 3)
# my_tuple[0] = 99  # This would cause an error!
```

---

## 🏆 Quick Knowledge Check

Test your understanding:

1. **What data type is the result of `5 / 2`?**
   - A) int
   - B) float
   - C) str

2. **Which of these creates an empty dictionary?**
   - A) `[]`
   - B) `{}`
   - C) `()`

3. **What does `bool("")` return?**
   - A) True
   - B) False
   - C) Error

**Answers:** 1-B, 2-B, 3-B

---

## 🎉 Congratulations!

You now understand Python's data types! This knowledge forms the foundation for everything else you'll learn in Python.

**Key Takeaways:**
- ✅ Different data types serve different purposes
- ✅ Python automatically determines types, but you can convert between them
- ✅ Understanding types helps prevent bugs and write better code
- ✅ Practice with real examples to solidify your knowledge

## 🚀 What's Next?

Now that you understand data types, you're ready to learn about **operators** - the tools that let you manipulate and work with your data in powerful ways.

**Continue Learning**: [Python Operators](operators.md) → [Practice with Operators](../../_3Operators.ipynb)

---

**💡 Pro Tip**: When in doubt about a data type, use the `type()` function to check. It's a programmer's best friend for debugging type-related issues!