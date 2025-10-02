# Python Control Flow - Making Decisions and Loops 🔀

## Introduction

Control flow is the order in which statements are executed in a program. It's what makes your code intelligent - allowing it to make decisions, repeat actions, and respond to different situations. Master control flow, and you'll be able to write programs that truly think and adapt!

## 🎯 Learning Objectives

After completing this lesson, you will:
- Use conditional statements to make decisions
- Create loops to repeat code efficiently
- Control loop execution with break and continue
- Handle exceptions gracefully
- Build complex program logic
- Write clean, readable control flow code

---

## 🤔 Conditional Statements

Conditional statements allow your program to make decisions based on different conditions.

### The `if` Statement

The basic building block of decision-making:

```python
age = 18

if age >= 18:
    print("You are an adult!")
    print("You can vote!")
```

### The `if-else` Statement

Provide an alternative when the condition is false:

```python
temperature = 25

if temperature > 30:
    print("It's hot! Stay hydrated.")
else:
    print("Nice weather today!")
```

### The `if-elif-else` Statement

Handle multiple conditions:

```python
grade = 85

if grade >= 90:
    letter_grade = "A"
    message = "Excellent work!"
elif grade >= 80:
    letter_grade = "B"
    message = "Good job!"
elif grade >= 70:
    letter_grade = "C"
    message = "You passed!"
elif grade >= 60:
    letter_grade = "D"
    message = "You need to improve"
else:
    letter_grade = "F"
    message = "You failed. Study harder!"

print(f"Grade: {letter_grade} - {message}")
```

### Practical Example: Smart Traffic Light System
```python
def traffic_light_decision(time_of_day, traffic_density, emergency_vehicle=False):
    """Smart traffic light system that adapts to conditions"""
    
    # Emergency vehicles get immediate priority
    if emergency_vehicle:
        return {
            "light": "GREEN",
            "duration": 30,
            "message": "🚨 Emergency vehicle detected - clearing traffic"
        }
    
    # Rush hour logic (7-9 AM, 5-7 PM)
    if (7 <= time_of_day <= 9) or (17 <= time_of_day <= 19):
        if traffic_density >= 80:
            duration = 90  # Longer green for heavy traffic
            message = "🚦 Rush hour - extended green time"
        elif traffic_density >= 50:
            duration = 60
            message = "🚦 Rush hour - normal timing"
        else:
            duration = 45
            message = "🚦 Rush hour - light traffic"
    
    # Night time (10 PM - 6 AM)
    elif time_of_day >= 22 or time_of_day <= 6:
        if traffic_density <= 10:
            duration = 30  # Shorter cycles at night
            message = "🌙 Night mode - quick cycling"
        else:
            duration = 45
            message = "🌙 Night mode - some traffic"
    
    # Regular daytime hours
    else:
        if traffic_density >= 70:
            duration = 75
            message = "☀️ Daytime - heavy traffic"
        elif traffic_density >= 30:
            duration = 60
            message = "☀️ Daytime - moderate traffic"
        else:
            duration = 45
            message = "☀️ Daytime - light traffic"
    
    return {
        "light": "GREEN",
        "duration": duration,
        "message": message
    }

# Test different scenarios
test_scenarios = [
    {"time": 8, "density": 85, "emergency": False, "desc": "Morning rush hour, heavy traffic"},
    {"time": 2, "density": 5, "emergency": False, "desc": "Late night, minimal traffic"},
    {"time": 14, "density": 45, "emergency": True, "desc": "Afternoon with emergency vehicle"},
    {"time": 18, "density": 60, "emergency": False, "desc": "Evening rush hour"},
]

for scenario in test_scenarios:
    result = traffic_light_decision(
        scenario["time"], 
        scenario["density"], 
        scenario["emergency"]
    )
    print(f"\nScenario: {scenario['desc']}")
    print(f"Decision: {result['message']}")
    print(f"Green light duration: {result['duration']} seconds")
```

---

## 🔄 Loops

Loops allow you to repeat code efficiently, avoiding duplication and enabling powerful automation.

### The `for` Loop

Best for iterating over sequences or when you know the number of iterations:

```python
# Iterating over a list
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(f"I like {fruit}")

# Iterating over a range
for i in range(5):
    print(f"Count: {i}")

# Iterating with index and value
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# Iterating over dictionary
student = {"name": "Alice", "age": 20, "grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}")
```

### The `while` Loop

Best when the number of iterations is unknown or depends on a condition:

```python
# Basic while loop
count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1

# Interactive loop
user_input = ""
while user_input.lower() != "quit":
    user_input = input("Enter a command (or 'quit' to exit): ")
    if user_input.lower() != "quit":
        print(f"You entered: {user_input}")

print("Goodbye!")
```

### Practical Example: Password Strength Checker
```python
import re

def check_password_strength(password):
    """Check password strength and return score and feedback"""
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 12:
        score += 3
        feedback.append("✅ Good length (12+ characters)")
    elif len(password) >= 8:
        score += 2
        feedback.append("⚠️ Adequate length (8+ characters)")
    else:
        feedback.append("❌ Too short (minimum 8 characters)")
    
    # Character variety checks
    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("✅ Contains lowercase letters")
    else:
        feedback.append("❌ Missing lowercase letters")
    
    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("✅ Contains uppercase letters")
    else:
        feedback.append("❌ Missing uppercase letters")
    
    if re.search(r'\d', password):
        score += 1
        feedback.append("✅ Contains numbers")
    else:
        feedback.append("❌ Missing numbers")
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 2
        feedback.append("✅ Contains special characters")
    else:
        feedback.append("❌ Missing special characters")
    
    # Determine strength level
    if score >= 7:
        strength = "Very Strong"
        color = "🟢"
    elif score >= 5:
        strength = "Strong"
        color = "🟡"
    elif score >= 3:
        strength = "Moderate"
        color = "🟠"
    else:
        strength = "Weak"
        color = "🔴"
    
    return {
        "score": score,
        "max_score": 8,
        "strength": strength,
        "color": color,
        "feedback": feedback
    }

def password_creation_assistant():
    """Interactive password creation with real-time feedback"""
    print("🔐 Password Creation Assistant")
    print("=" * 40)
    
    while True:
        password = input("\nEnter a password (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("👋 Goodbye! Stay secure!")
            break
        
        if not password:
            print("❌ Please enter a password")
            continue
        
        # Check password strength
        result = check_password_strength(password)
        
        print(f"\n{result['color']} Password Strength: {result['strength']}")
        print(f"📊 Score: {result['score']}/{result['max_score']}")
        print("\nFeedback:")
        
        for item in result['feedback']:
            print(f"  {item}")
        
        if result['score'] >= 7:
            print(f"\n🎉 Excellent! Your password is {result['strength'].lower()}.")
            break
        elif result['score'] >= 5:
            print(f"\n✅ Good! Your password is {result['strength'].lower()}.")
            print("💡 Tip: Add more special characters for maximum security.")
        else:
            print(f"\n⚠️ Your password is {result['strength'].lower()}. Please improve it.")

# Run the assistant (commented out for documentation)
# password_creation_assistant()

# Test with sample passwords
test_passwords = [
    "password123",
    "MySecureP@ssw0rd!",
    "abc123",
    "SuperSecure2023!@#"
]

print("Password Strength Test Results:")
print("=" * 50)

for pwd in test_passwords:
    result = check_password_strength(pwd)
    print(f"\nPassword: {'*' * len(pwd)}")
    print(f"Strength: {result['color']} {result['strength']} ({result['score']}/{result['max_score']})")
```

---

## 🎛️ Loop Control: `break` and `continue`

Control the flow within loops using `break` and `continue` statements.

### The `break` Statement
Exits the loop immediately:

```python
# Finding the first even number
numbers = [1, 3, 7, 8, 11, 12, 15]

for num in numbers:
    if num % 2 == 0:
        print(f"First even number found: {num}")
        break
    print(f"Checking: {num}")
```

### The `continue` Statement
Skips the rest of the current iteration:

```python
# Processing only positive numbers
numbers = [-2, 5, -1, 8, -3, 10, 0, 7]

print("Processing only positive numbers:")
for num in numbers:
    if num <= 0:
        continue  # Skip non-positive numbers
    
    result = num ** 2
    print(f"{num}² = {result}")
```

### Practical Example: Data Cleaning Pipeline
```python
def clean_and_process_data(raw_data):
    """Clean and process a dataset with error handling"""
    
    cleaned_data = []
    skipped_count = 0
    processed_count = 0
    
    print("🧹 Starting data cleaning process...")
    print("=" * 40)
    
    for i, record in enumerate(raw_data):
        print(f"\nProcessing record {i + 1}: {record}")
        
        # Skip empty records
        if not record or record.strip() == "":
            print("  ⏭️ Skipping: Empty record")
            skipped_count += 1
            continue
        
        # Skip records with invalid format
        if not isinstance(record, str):
            print("  ⏭️ Skipping: Not a string")
            skipped_count += 1
            continue
        
        # Clean the record
        cleaned_record = record.strip().lower()
        
        # Skip records that are too short
        if len(cleaned_record) < 2:
            print("  ⏭️ Skipping: Too short")
            skipped_count += 1
            continue
        
        # Skip records with numbers (assuming we want text only)
        if any(char.isdigit() for char in cleaned_record):
            print("  ⏭️ Skipping: Contains numbers")
            skipped_count += 1
            continue
        
        # Process valid record
        processed_record = {
            "original": record,
            "cleaned": cleaned_record,
            "length": len(cleaned_record),
            "word_count": len(cleaned_record.split())
        }
        
        cleaned_data.append(processed_record)
        processed_count += 1
        print(f"  ✅ Processed: '{cleaned_record}'")
        
        # Stop if we have enough clean data
        if processed_count >= 10:
            print("\n🛑 Reached maximum processed records limit (10)")
            break
    
    print(f"\n📊 Data Cleaning Summary:")
    print(f"  Total records: {len(raw_data)}")
    print(f"  Successfully processed: {processed_count}")
    print(f"  Skipped: {skipped_count}")
    print(f"  Success rate: {processed_count / len(raw_data) * 100:.1f}%")
    
    return cleaned_data

# Test the data cleaning pipeline
sample_data = [
    "  Hello World  ",
    "Python Programming",
    "",
    "Data Science",
    "test123",
    "AI",
    None,
    "Machine Learning",
    "  ",
    "Deep Learning",
    "NLP",
    "Computer Vision",
    "data4you",
    "Statistics",
    "Mathematics"
]

cleaned_results = clean_and_process_data(sample_data)

print(f"\n🎉 Final cleaned dataset ({len(cleaned_results)} records):")
for i, record in enumerate(cleaned_results, 1):
    print(f"{i:2d}. {record['cleaned']} (words: {record['word_count']})")
```

---

## 🎯 Nested Loops

Loops inside loops for handling multi-dimensional data:

```python
# Creating a multiplication table
print("📊 Multiplication Table (1-10)")
print("   ", end="")
for i in range(1, 11):
    print(f"{i:4d}", end="")
print()

for i in range(1, 11):
    print(f"{i:2d}:", end="")
    for j in range(1, 11):
        product = i * j
        print(f"{product:4d}", end="")
    print()  # New line after each row
```

### Practical Example: Seating Chart Generator
```python
def generate_seating_chart(rows, seats_per_row, reserved_seats=None, vip_rows=None):
    """Generate a dynamic seating chart with reservations and VIP sections"""
    
    if reserved_seats is None:
        reserved_seats = []
    if vip_rows is None:
        vip_rows = []
    
    print("🎭 THEATER SEATING CHART")
    print("=" * (seats_per_row * 4 + 10))
    print("🎬 SCREEN")
    print("=" * (seats_per_row * 4 + 10))
    
    seating_stats = {
        "total_seats": rows * seats_per_row,
        "available": 0,
        "reserved": len(reserved_seats),
        "vip_total": len(vip_rows) * seats_per_row if vip_rows else 0
    }
    
    for row in range(1, rows + 1):
        # Determine row type
        if row in vip_rows:
            row_prefix = "VIP"
            seat_symbol = "💺"
        else:
            row_prefix = f"R{row:2d}"
            seat_symbol = "🪑"
        
        print(f"{row_prefix}: ", end="")
        
        for seat in range(1, seats_per_row + 1):
            seat_id = f"{row}-{seat}"
            
            # Check if seat is reserved
            if seat_id in reserved_seats:
                print(" ❌ ", end="")
            # VIP seats
            elif row in vip_rows:
                print(f" {seat_symbol} ", end="")
                if seat_id not in reserved_seats:
                    seating_stats["available"] += 1
            # Regular available seats
            else:
                print(f" {seat_symbol} ", end="")
                seating_stats["available"] += 1
        
        # Add row labels on the right
        if row in vip_rows:
            print(f"  👑 VIP Row {row}")
        else:
            print(f"  Row {row}")
    
    # Print legend and statistics
    print("\n" + "=" * (seats_per_row * 4 + 10))
    print("LEGEND: 🪑 Available  💺 VIP Available  ❌ Reserved")
    print(f"\n📊 SEATING STATISTICS:")
    print(f"  Total Seats: {seating_stats['total_seats']}")
    print(f"  Available: {seating_stats['available']}")
    print(f"  Reserved: {seating_stats['reserved']}")
    print(f"  VIP Seats: {seating_stats['vip_total']}")
    print(f"  Occupancy: {seating_stats['reserved'] / seating_stats['total_seats'] * 100:.1f}%")
    
    return seating_stats

# Generate sample seating chart
reserved_list = ["1-3", "1-4", "2-5", "2-6", "3-1", "5-7", "5-8"]
vip_list = [1, 2]

stats = generate_seating_chart(
    rows=8,
    seats_per_row=10,
    reserved_seats=reserved_list,
    vip_rows=vip_list
)
```

---

## 🛡️ Exception Handling

Handle errors gracefully using try-except blocks:

### Basic Exception Handling
```python
try:
    # Code that might raise an exception
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"10 divided by {number} is {result}")
    
except ValueError:
    print("❌ Please enter a valid number!")
    
except ZeroDivisionError:
    print("❌ Cannot divide by zero!")
    
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
    
else:
    print("✅ Calculation completed successfully!")
    
finally:
    print("🏁 Program finished.")
```

### Practical Example: Robust File Processing System
```python
import json
import os
from datetime import datetime

def process_data_file(filename):
    """Robust file processing with comprehensive error handling"""
    
    processing_log = {
        "filename": filename,
        "timestamp": datetime.now().isoformat(),
        "status": "unknown",
        "records_processed": 0,
        "errors": [],
        "warnings": []
    }
    
    try:
        # Check if file exists
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File '{filename}' not found")
        
        # Check file size
        file_size = os.path.getsize(filename)
        if file_size == 0:
            processing_log["warnings"].append("File is empty")
            processing_log["status"] = "warning"
            return processing_log
        
        print(f"📁 Processing file: {filename} ({file_size} bytes)")
        
        with open(filename, 'r', encoding='utf-8') as file:
            try:
                # Attempt to load as JSON
                data = json.load(file)
                
                if not isinstance(data, list):
                    processing_log["warnings"].append("Data is not a list, wrapping in list")
                    data = [data]
                
                # Process each record
                for i, record in enumerate(data):
                    try:
                        # Validate record structure
                        if not isinstance(record, dict):
                            error_msg = f"Record {i+1} is not a dictionary, skipping"
                            processing_log["errors"].append(error_msg)
                            continue
                        
                        # Required fields check
                        required_fields = ["id", "name"]
                        missing_fields = [field for field in required_fields if field not in record]
                        
                        if missing_fields:
                            error_msg = f"Record {i+1} missing fields: {missing_fields}"
                            processing_log["errors"].append(error_msg)
                            continue
                        
                        # Process valid record
                        processed_record = {
                            "id": record["id"],
                            "name": record["name"].strip().title(),
                            "processed_at": datetime.now().isoformat(),
                            "record_number": i + 1
                        }
                        
                        # Add optional fields if present
                        if "email" in record:
                            processed_record["email"] = record["email"].lower().strip()
                        
                        processing_log["records_processed"] += 1
                        print(f"  ✅ Processed record {i+1}: {processed_record['name']}")
                        
                    except KeyError as e:
                        error_msg = f"Record {i+1} - Key error: {e}"
                        processing_log["errors"].append(error_msg)
                        print(f"  ❌ {error_msg}")
                        continue
                    
                    except ValueError as e:
                        error_msg = f"Record {i+1} - Value error: {e}"
                        processing_log["errors"].append(error_msg)
                        print(f"  ❌ {error_msg}")
                        continue
                
            except json.JSONDecodeError as e:
                # Not a JSON file, try processing as text
                processing_log["warnings"].append("Not a JSON file, processing as text")
                file.seek(0)  # Reset file pointer
                
                line_count = 0
                for line_num, line in enumerate(file, 1):
                    try:
                        line = line.strip()
                        if line:  # Skip empty lines
                            # Simple text processing
                            print(f"  📝 Line {line_num}: {line[:50]}{'...' if len(line) > 50 else ''}")
                            line_count += 1
                    except UnicodeDecodeError as e:
                        error_msg = f"Line {line_num} - Encoding error: {e}"
                        processing_log["errors"].append(error_msg)
                        continue
                
                processing_log["records_processed"] = line_count
    
    except FileNotFoundError as e:
        processing_log["status"] = "error"
        processing_log["errors"].append(f"File not found: {e}")
        print(f"❌ File error: {e}")
        return processing_log
    
    except PermissionError as e:
        processing_log["status"] = "error"
        processing_log["errors"].append(f"Permission denied: {e}")
        print(f"❌ Permission error: {e}")
        return processing_log
    
    except Exception as e:
        processing_log["status"] = "error"
        processing_log["errors"].append(f"Unexpected error: {str(e)}")
        print(f"❌ Unexpected error: {e}")
        return processing_log
    
    else:
        # Success case
        if processing_log["errors"]:
            processing_log["status"] = "completed_with_errors"
        elif processing_log["warnings"]:
            processing_log["status"] = "completed_with_warnings"
        else:
            processing_log["status"] = "success"
        
        print(f"✅ File processing completed!")
    
    finally:
        # Cleanup and reporting
        print(f"\n📊 Processing Summary for '{filename}':")
        print(f"  Status: {processing_log['status']}")
        print(f"  Records processed: {processing_log['records_processed']}")
        print(f"  Errors: {len(processing_log['errors'])}")
        print(f"  Warnings: {len(processing_log['warnings'])}")
        
        if processing_log['errors']:
            print("  Error details:")
            for error in processing_log['errors'][:3]:  # Show first 3 errors
                print(f"    - {error}")
            if len(processing_log['errors']) > 3:
                print(f"    ... and {len(processing_log['errors']) - 3} more errors")
    
    return processing_log

# Create sample test files for demonstration
sample_json_data = [
    {"id": 1, "name": "Alice Johnson", "email": "alice@example.com"},
    {"id": 2, "name": "bob smith", "email": "BOB@EXAMPLE.COM"},
    {"id": 3, "name": "  charlie brown  "},
    {"name": "Missing ID"},  # This will cause an error
    {"id": 5, "name": "Eve Wilson", "email": "eve@example.com"}
]

# Save sample data (commented out for documentation)
# with open("sample_data.json", "w") as f:
#     json.dump(sample_json_data, f, indent=2)

# Test the processing system
print("🧪 Testing File Processing System")
print("=" * 50)

# This would process the actual file
# result = process_data_file("sample_data.json")
```

---

## 🚀 Interactive Practice

Ready to master Python control flow? Click below to open an interactive environment:

[![Practice Control Flow](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/leekwansoo/python-excercise/main?labpath=notebooks/_4ControlFlow.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/leekwansoo/python-excercise/blob/main/notebooks/_4ControlFlow.ipynb)

**In the interactive notebook, you'll:**
- Build decision-making programs step-by-step
- Create efficient loops for data processing
- Practice exception handling with real scenarios
- Develop complex control flow applications

---

## ⚠️ Common Control Flow Pitfalls

### 1. Indentation Errors
```python
# Wrong - inconsistent indentation
if True:
    print("This is correct")
  print("This will cause an IndentationError!")

# Correct - consistent indentation
if True:
    print("This is correct")
    print("This is also correct")
```

### 2. Infinite Loops
```python
# Dangerous - infinite loop
count = 0
while count < 10:
    print(count)
    # Forgot to increment count!

# Safe - proper increment
count = 0
while count < 10:
    print(count)
    count += 1  # Don't forget this!
```

### 3. Mutable Default Arguments in Loops
```python
# Problem - unexpected behavior
results = []
for i in range(3):
    results.append([])  # Create new list each time
    results[i].append(i)

# This works correctly: [[0], [1], [2]]
```

### 4. Exception Handling Anti-patterns
```python
# Bad - catching all exceptions
try:
    # some code
    pass
except:  # Don't do this!
    pass

# Good - specific exception handling
try:
    # some code
    pass
except ValueError as e:
    print(f"Value error: {e}")
except FileNotFoundError as e:
    print(f"File not found: {e}")
```

---

## 🏆 Quick Knowledge Check

Test your control flow mastery:

1. **What happens if you don't include a `break` in an infinite loop?**
   - A) The program stops after 1000 iterations
   - B) The program runs forever
   - C) Python automatically adds a break

2. **Which statement skips the rest of the current loop iteration?**
   - A) `break`
   - B) `continue`  
   - C) `pass`

3. **What does the `else` clause in a `for` loop do?**
   - A) Runs if the loop encounters an error
   - B) Runs if the loop completes normally (no break)
   - C) Never runs

4. **What's the best way to handle multiple specific exceptions?**
   - A) Use multiple `try-except` blocks
   - B) Use multiple `except` clauses
   - C) Use a single `except Exception`

**Answers:** 1-B, 2-B, 3-B, 4-B

---

## 🎉 Congratulations!

You've mastered Python control flow! You can now create programs that make intelligent decisions, process data efficiently, and handle errors gracefully.

**Key Takeaways:**
- ✅ Conditional statements enable decision-making
- ✅ Loops automate repetitive tasks efficiently
- ✅ Loop control statements provide fine-grained control
- ✅ Exception handling makes programs robust
- ✅ Proper control flow creates maintainable code

## 🚀 What's Next?

With control flow mastered, you're ready to learn about **functions** - how to organize your code into reusable, modular pieces.

**Continue Learning**: [Functions](functions.md) → [Practice Functions](../../notebooks/_5Functions.ipynb)

---

**💡 Pro Tip**: Always think about edge cases when designing control flow. What happens with empty data? Invalid input? Network failures? Robust programs anticipate and handle these scenarios gracefully!