# Python Operators - The Tools of Programming 🛠️

## Introduction

Operators are symbols that perform operations on variables and values. They are the fundamental tools that allow you to manipulate data, make comparisons, and control the flow of your programs. Think of them as the verbs in the language of programming!

## 🎯 Learning Objectives

After completing this lesson, you will:
- Master all Python operator types
- Understand operator precedence and associativity
- Use operators to solve real-world problems
- Combine operators for complex expressions
- Write more efficient and readable code

---

## 📊 Types of Python Operators

Python provides several categories of operators:

| Category | Operators | Purpose |
|----------|-----------|---------|
| **Arithmetic** | `+`, `-`, `*`, `/`, `//`, `%`, `**` | Mathematical calculations |
| **Assignment** | `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` | Assign and modify values |
| **Comparison** | `==`, `!=`, `>`, `<`, `>=`, `<=` | Compare values |
| **Logical** | `and`, `or`, `not` | Combine boolean expressions |
| **Identity** | `is`, `is not` | Test object identity |
| **Membership** | `in`, `not in` | Test membership in sequences |
| **Bitwise** | `&`, `\|`, `^`, `~`, `<<`, `>>` | Bit-level operations |

---

## ➕ Arithmetic Operators

These operators perform mathematical calculations:

### Basic Operations:
```python
a = 10
b = 3

print(f"Addition: {a} + {b} = {a + b}")        # 13
print(f"Subtraction: {a} - {b} = {a - b}")     # 7
print(f"Multiplication: {a} * {b} = {a * b}")  # 30
print(f"Division: {a} / {b} = {a / b}")        # 3.3333...
print(f"Floor Division: {a} // {b} = {a // b}") # 3
print(f"Modulus: {a} % {b} = {a % b}")         # 1
print(f"Exponentiation: {a} ** {b} = {a ** b}") # 1000
```

### Practical Examples:

#### Example 1: Temperature Conversion
```python
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Test the conversion
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")  # 25°C = 77.0°F
```

#### Example 2: Calculate Circle Properties
```python
import math

def circle_properties(radius):
    """Calculate area and circumference of a circle"""
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

r = 5
area, circumference = circle_properties(r)
print(f"Circle with radius {r}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
```

---

## 📝 Assignment Operators

Assignment operators assign values to variables and can combine assignment with arithmetic operations:

### Basic Assignment:
```python
x = 10          # Simple assignment
print(x)        # 10
```

### Compound Assignment (Shorthand):
```python
score = 100

# Traditional way vs compound assignment
score = score + 5    # Traditional
score += 5           # Compound (same result)

# All compound assignment operators
score += 10    # score = score + 10
score -= 5     # score = score - 5
score *= 2     # score = score * 2
score /= 3     # score = score / 3
score //= 2    # score = score // 2
score %= 7     # score = score % 7
score **= 2    # score = score ** 2

print(f"Final score: {score}")
```

### Practical Example: Bank Account
```python
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def deposit(self, amount):
        self.balance += amount  # Using += operator
        return self.balance
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount  # Using -= operator
            return self.balance
        else:
            print("Insufficient funds!")
            return self.balance

# Test the account
account = BankAccount(1000)
print(f"Initial balance: ${account.balance}")

account.deposit(250)
print(f"After deposit: ${account.balance}")

account.withdraw(100)
print(f"After withdrawal: ${account.balance}")
```

---

## 🔍 Comparison Operators

Comparison operators compare values and return boolean results:

```python
a = 10
b = 5
c = 10

# Equality and inequality
print(f"{a} == {c}: {a == c}")  # True
print(f"{a} != {b}: {a != b}")  # True

# Greater than and less than
print(f"{a} > {b}: {a > b}")    # True
print(f"{a} < {b}: {a < b}")    # False
print(f"{a} >= {c}: {a >= c}")  # True
print(f"{a} <= {b}: {a <= b}")  # False

# Chaining comparisons
age = 25
print(f"18 <= {age} <= 65: {18 <= age <= 65}")  # True
```

### Practical Example: Grade Calculator
```python
def get_letter_grade(score):
    """Convert numeric score to letter grade"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def evaluate_performance(score):
    """Evaluate student performance"""
    letter = get_letter_grade(score)
    
    if score >= 95:
        performance = "Excellent!"
    elif score >= 85:
        performance = "Very Good"
    elif score >= 75:
        performance = "Good"
    elif score >= 65:
        performance = "Satisfactory"
    else:
        performance = "Needs Improvement"
    
    return letter, performance

# Test with different scores
test_scores = [98, 87, 76, 65, 45]
for score in test_scores:
    grade, performance = evaluate_performance(score)
    print(f"Score: {score} → Grade: {grade} ({performance})")
```

---

## 🧠 Logical Operators

Logical operators combine or modify boolean expressions:

### Basic Logical Operations:
```python
# and operator (both conditions must be True)
print(f"True and True: {True and True}")    # True
print(f"True and False: {True and False}")  # False

# or operator (at least one condition must be True)
print(f"True or False: {True or False}")    # True
print(f"False or False: {False or False}")  # False

# not operator (reverses the boolean value)
print(f"not True: {not True}")              # False
print(f"not False: {not False}")            # True
```

### Practical Example: Access Control System
```python
def check_access(age, has_id, is_member, is_vip=False):
    """Check if person can access the facility"""
    
    # Basic access requirements
    basic_access = age >= 18 and has_id
    
    # Membership access
    member_access = is_member and basic_access
    
    # VIP access (special privileges)
    vip_access = is_vip or (member_access and age >= 21)
    
    # Restricted areas (only for VIP members over 25)
    restricted_access = is_vip and age >= 25 and is_member
    
    return {
        "basic_access": basic_access,
        "member_access": member_access,
        "vip_access": vip_access,
        "restricted_access": restricted_access
    }

# Test different scenarios
scenarios = [
    {"name": "John", "age": 19, "has_id": True, "is_member": True, "is_vip": False},
    {"name": "Alice", "age": 26, "has_id": True, "is_member": True, "is_vip": True},
    {"name": "Bob", "age": 17, "has_id": True, "is_member": False, "is_vip": False},
]

for person in scenarios:
    access = check_access(
        person["age"], 
        person["has_id"], 
        person["is_member"], 
        person["is_vip"]
    )
    print(f"\n{person['name']} (Age: {person['age']}):")
    for level, granted in access.items():
        status = "✅ Granted" if granted else "❌ Denied"
        print(f"  {level.replace('_', ' ').title()}: {status}")
```

---

## 🆔 Identity and Membership Operators

### Identity Operators (`is`, `is not`):
Test if two variables refer to the same object in memory:

```python
# Identity operators
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a is b: {a is b}")       # False (different objects)
print(f"a is c: {a is c}")       # True (same object)
print(f"a == b: {a == b}")       # True (same content)

# Common use with None
value = None
if value is None:
    print("Value is None")

# Be careful with small integers and strings (Python optimizes these)
x = 5
y = 5
print(f"x is y: {x is y}")       # True (Python caches small integers)
```

### Membership Operators (`in`, `not in`):
Test if a value exists in a sequence:

```python
# Membership in lists
fruits = ["apple", "banana", "cherry"]
print(f"'apple' in fruits: {'apple' in fruits}")           # True
print(f"'orange' not in fruits: {'orange' not in fruits}") # True

# Membership in strings
text = "Python Programming"
print(f"'Python' in text: {'Python' in text}")            # True
print(f"'Java' not in text: {'Java' not in text}")        # True

# Membership in dictionaries (checks keys)
student = {"name": "Alice", "age": 20, "grade": "A"}
print(f"'name' in student: {'name' in student}")          # True
print(f"'Alice' in student: {'Alice' in student}")        # False (checks keys, not values)
```

### Practical Example: Content Filter
```python
def content_filter(text, banned_words, required_words=None):
    """Filter content based on banned and required words"""
    
    # Convert to lowercase for case-insensitive checking
    text_lower = text.lower()
    
    # Check for banned words
    has_banned = any(word.lower() in text_lower for word in banned_words)
    
    # Check for required words (if specified)
    has_required = True
    if required_words:
        has_required = all(word.lower() in text_lower for word in required_words)
    
    # Determine if content passes filter
    passes_filter = not has_banned and has_required
    
    return {
        "passes_filter": passes_filter,
        "has_banned_content": has_banned,
        "has_required_content": has_required,
        "banned_found": [word for word in banned_words if word.lower() in text_lower],
        "required_missing": [word for word in (required_words or []) if word.lower() not in text_lower]
    }

# Test the content filter
test_content = "This is a great Python tutorial for beginners"
banned = ["spam", "fake", "scam"]
required = ["Python", "tutorial"]

result = content_filter(test_content, banned, required)
print(f"Content: '{test_content}'")
print(f"Passes filter: {result['passes_filter']}")
print(f"Banned words found: {result['banned_found']}")
print(f"Required words missing: {result['required_missing']}")
```

---

## ⚖️ Operator Precedence and Associativity

Understanding the order in which operators are evaluated is crucial for writing correct expressions:

### Precedence Order (Highest to Lowest):
```python
# 1. Parentheses (highest precedence)
result = (2 + 3) * 4  # = 5 * 4 = 20

# 2. Exponentiation (**)
result = 2 ** 3 ** 2  # = 2 ** (3 ** 2) = 2 ** 9 = 512

# 3. Unary operators (+, -, not)
result = -3 ** 2      # = -(3 ** 2) = -9

# 4. Multiplication, Division, Modulus (*, /, //, %)
result = 10 + 2 * 3   # = 10 + (2 * 3) = 16

# 5. Addition, Subtraction (+, -)
result = 10 - 2 + 3   # = (10 - 2) + 3 = 11 (left to right)

# 6. Comparison operators (==, !=, <, >, <=, >=)
# 7. Identity and membership operators (is, is not, in, not in)
# 8. Logical NOT (not)
# 9. Logical AND (and)
# 10. Logical OR (or) (lowest precedence)
```

### Practical Example: Complex Expression
```python
def calculate_final_price(base_price, tax_rate, discount_percent, is_member):
    """Calculate final price with complex pricing rules"""
    
    # Using proper operator precedence
    # 1. Calculate discount amount
    discount_amount = base_price * discount_percent / 100
    
    # 2. Apply member discount (additional 5% if member)
    member_discount = base_price * 0.05 if is_member else 0
    
    # 3. Calculate price after discounts
    discounted_price = base_price - discount_amount - member_discount
    
    # 4. Calculate tax on discounted price
    tax_amount = discounted_price * tax_rate / 100
    
    # 5. Final price
    final_price = discounted_price + tax_amount
    
    return {
        "base_price": base_price,
        "discount_amount": discount_amount,
        "member_discount": member_discount,
        "discounted_price": discounted_price,
        "tax_amount": tax_amount,
        "final_price": final_price
    }

# Test the calculation
price_breakdown = calculate_final_price(
    base_price=100.00,
    tax_rate=8.5,
    discount_percent=15,
    is_member=True
)

print("Price Breakdown:")
for key, value in price_breakdown.items():
    print(f"  {key.replace('_', ' ').title()}: ${value:.2f}")
```

---

## 🎯 Real-World Applications

### Example 1: Smart Home Security System
```python
class SmartHomeSecurity:
    def __init__(self):
        self.armed = False
        self.motion_detected = False
        self.door_open = False
        self.window_open = False
        self.owner_home = False
    
    def evaluate_threat_level(self):
        """Evaluate security threat using multiple operators"""
        
        # High threat conditions
        high_threat = (
            self.armed and 
            (self.motion_detected or self.door_open or self.window_open) and 
            not self.owner_home
        )
        
        # Medium threat conditions  
        medium_threat = (
            not high_threat and
            self.armed and
            (self.motion_detected or self.door_open or self.window_open)
        )
        
        # Low threat conditions
        low_threat = (
            not high_threat and 
            not medium_threat and
            (self.motion_detected or self.door_open or self.window_open)
        )
        
        return {
            "high_threat": high_threat,
            "medium_threat": medium_threat,
            "low_threat": low_threat,
            "no_threat": not (high_threat or medium_threat or low_threat)
        }
    
    def get_recommended_action(self):
        """Get recommended action based on threat level"""
        threat = self.evaluate_threat_level()
        
        if threat["high_threat"]:
            return "🚨 ALERT: Call security! Potential break-in detected."
        elif threat["medium_threat"]:
            return "⚠️ WARNING: Unusual activity detected while armed."
        elif threat["low_threat"]:
            return "ℹ️ INFO: Activity detected (system not armed)."
        else:
            return "✅ All clear - no threats detected."

# Test different scenarios
security = SmartHomeSecurity()

scenarios = [
    {"name": "Break-in attempt", "armed": True, "motion": True, "door": True, "owner": False},
    {"name": "Owner returning", "armed": True, "motion": True, "door": True, "owner": True},
    {"name": "Cat walking around", "armed": False, "motion": True, "door": False, "owner": False},
    {"name": "All quiet", "armed": True, "motion": False, "door": False, "owner": False},
]

for scenario in scenarios:
    security.armed = scenario["armed"]
    security.motion_detected = scenario["motion"]
    security.door_open = scenario["door"]
    security.owner_home = scenario["owner"]
    
    print(f"\nScenario: {scenario['name']}")
    print(f"Action: {security.get_recommended_action()}")
```

### Example 2: E-commerce Recommendation Engine
```python
def recommend_products(user_age, purchase_history, current_season, budget, is_premium):
    """Product recommendation system using various operators"""
    
    recommendations = []
    
    # Age-based recommendations
    if user_age >= 18 and user_age <= 30:
        youth_products = ["Smartphone", "Gaming Console", "Trendy Clothes"]
        recommendations.extend(youth_products)
    elif user_age > 30 and user_age <= 50:
        adult_products = ["Kitchen Appliances", "Professional Attire", "Home Decor"]
        recommendations.extend(adult_products)
    elif user_age > 50:
        mature_products = ["Garden Tools", "Books", "Comfortable Furniture"]
        recommendations.extend(mature_products)
    
    # Purchase history analysis
    if "Electronics" in purchase_history:
        recommendations += ["Latest Gadgets", "Tech Accessories"]
    
    if "Clothing" in purchase_history:
        recommendations += ["Fashion Items", "Accessories"]
    
    # Seasonal recommendations
    season_products = {
        "spring": ["Gardening Supplies", "Light Jackets"],
        "summer": ["Beach Gear", "Summer Clothes"],
        "autumn": ["Warm Clothes", "School Supplies"],
        "winter": ["Winter Gear", "Holiday Gifts"]
    }
    
    if current_season in season_products:
        recommendations.extend(season_products[current_season])
    
    # Budget filtering
    if budget >= 1000:
        recommendations += ["Premium Items", "Luxury Goods"]
    elif budget >= 500:
        recommendations += ["Mid-range Products"]
    else:
        recommendations = [item for item in recommendations if "Premium" not in item and "Luxury" not in item]
    
    # Premium member benefits
    if is_premium:
        recommendations += ["Exclusive Items", "Early Access Products"]
    
    # Remove duplicates and return
    return list(set(recommendations))

# Test the recommendation engine
user_profile = {
    "age": 28,
    "purchase_history": ["Electronics", "Clothing"],
    "season": "winter",
    "budget": 800,
    "premium": True
}

recommendations = recommend_products(
    user_profile["age"],
    user_profile["purchase_history"],
    user_profile["season"],
    user_profile["budget"],
    user_profile["premium"]
)

print(f"Recommendations for user (Age: {user_profile['age']}, Budget: ${user_profile['budget']}):")
for i, product in enumerate(recommendations, 1):
    print(f"{i}. {product}")
```

---

## 🚀 Interactive Practice

Ready to master Python operators? Click below to open an interactive environment:

[![Practice Operators](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/leekwansoo/python-excercise/main?labpath=_3Operators.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/leekwansoo/python-excercise/blob/main/_3Operators.ipynb)

**In the interactive notebook, you'll:**
- Practice all operator types with hands-on exercises
- Build complex expressions step-by-step
- Solve real-world problems using operators
- Learn to debug operator precedence issues

---

## ⚠️ Common Operator Pitfalls

### 1. Assignment vs Equality Confusion
```python
# Wrong - using assignment (=) instead of equality (==)
age = 18
if age = 18:  # SyntaxError!
    print("Adult")

# Correct - using equality operator
if age == 18:
    print("Adult")
```

### 2. Operator Precedence Mistakes
```python
# Problem - unexpected result due to precedence
result = 10 + 2 * 3  # Result: 16 (not 36!)

# Solution - use parentheses for clarity
result = (10 + 2) * 3  # Result: 36
```

### 3. Logical Operator Short-Circuiting
```python
def expensive_operation():
    print("This is expensive!")
    return True

# Short-circuiting behavior
result1 = True or expensive_operation()   # expensive_operation() not called
result2 = False and expensive_operation() # expensive_operation() not called
result3 = True and expensive_operation()  # expensive_operation() IS called
```

### 4. Identity vs Equality Confusion
```python
# Dangerous - comparing lists with 'is'
list1 = [1, 2, 3]
list2 = [1, 2, 3]

if list1 is list2:      # False - different objects
    print("Same object")

if list1 == list2:      # True - same content
    print("Same content")
```

---

## 🏆 Quick Knowledge Check

Test your operator mastery:

1. **What is the result of `3 + 4 * 2`?**
   - A) 14
   - B) 11
   - C) 10

2. **What does `5 // 2` return?**
   - A) 2.5
   - B) 2
   - C) 3

3. **What is the result of `not (True and False)`?**
   - A) True
   - B) False
   - C) Error

4. **Which operator has higher precedence?**
   - A) `+` (addition)
   - B) `*` (multiplication)
   - C) They're equal

**Answers:** 1-B, 2-B, 3-A, 4-B

---

## 🎉 Congratulations!

You've mastered Python operators! You now have the tools to perform calculations, make comparisons, and build complex logical expressions.

**Key Takeaways:**
- ✅ Arithmetic operators handle mathematical calculations
- ✅ Comparison operators enable decision-making
- ✅ Logical operators combine conditions effectively  
- ✅ Understanding precedence prevents bugs
- ✅ Operators are the building blocks of programming logic

## 🚀 What's Next?

With operators under your belt, you're ready to learn about **control flow** - how to make your programs make decisions and repeat actions.

**Continue Learning**: [Control Flow](control-flow.md) → [Practice Control Flow](../../notebooks/_4ControlFlow.ipynb)

---

**💡 Pro Tip**: When writing complex expressions, use parentheses liberally to make your intentions clear. Your future self (and your teammates) will thank you!