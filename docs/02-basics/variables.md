# Python Variables - Theory and Concepts

## Learning Objectives
After completing this module, you will be able to:
- Understand what variables are and how they work in Python
- Create and assign values to variables
- Follow Python naming conventions
- Distinguish between different variable types

## What are Variables?

Variables in Python are containers for storing data values. Unlike other programming languages, Python has no command for declaring a variable - it is created the moment you first assign a value to it.

### Key Concepts

1. **Dynamic Typing**: Python automatically determines the variable type
2. **Case Sensitive**: `myVar` and `myvar` are different variables
3. **Memory Management**: Python handles memory allocation automatically

## Variable Creation

In Python, variables are created when you assign a value:

```python
x = 5
name = "John"
is_student = True
```

## Naming Rules

Python variable names must follow these rules:

- Must start with a letter (a-z, A-Z) or underscore (_)
- Cannot start with a number
- Can contain letters, numbers, and underscores
- Case-sensitive
- Cannot be Python keywords

### Valid Examples:
```python
my_var = "Hello"
_private = 42
userName = "student"
value2 = 100
```

### Invalid Examples:
```python
2var = "Error"     # Cannot start with number
my-var = "Error"   # Cannot use hyphen
class = "Error"    # Cannot use Python keyword
```

## Variable Types

Python has several built-in variable types:

| Type | Description | Example |
|------|-------------|---------|
| int | Integer numbers | `x = 5` |
| float | Decimal numbers | `y = 3.14` |
| str | Text strings | `name = "Python"` |
| bool | Boolean values | `is_valid = True` |
| list | Ordered collections | `numbers = [1, 2, 3]` |
| dict | Key-value pairs | `person = {"name": "John"}` |

## Best Practices

1. **Use descriptive names**: `student_count` instead of `sc`
2. **Follow snake_case**: `my_variable` not `myVariable`
3. **Avoid single letters**: except for short loops
4. **Use constants in UPPERCASE**: `MAX_SIZE = 100`

## 🎯 Ready to Practice?

Now that you understand the theory, let's practice with interactive code!

[![Practice Variables](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/leekwansoo/python-excercise/main?labpath=_1variables.ipynb)

**In the interactive notebook, you'll:**
- Create your first variables
- Experiment with different data types
- Practice naming conventions
- See real Python output and error messages

## 📚 What's Next?

After mastering variables, continue to:
- [Data Types](../02-basics/data-types.md) - Deep dive into Python's type system
- [Operators](../02-basics/operators.md) - Learn to manipulate variables

---

**💡 Tip**: Keep the interactive notebook open alongside this guide for the best learning experience!