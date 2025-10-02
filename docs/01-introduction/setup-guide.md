# Python Environment Setup Guide 🔧

## Introduction

Before we dive into Python programming, let's set up a proper development environment. Don't worry - we'll guide you through multiple options, from quick cloud-based solutions to complete local installations.

## 🌩️ Option 1: Cloud-Based Learning (Recommended for Beginners)

**Perfect for**: First-time learners, trying Python without installation, accessing from multiple devices

### Advantages
- ✅ No installation required
- ✅ Works on any device with a web browser
- ✅ Pre-configured with all necessary libraries
- ✅ Automatic saving and sharing capabilities
- ✅ Consistent environment for all learners

### 🚀 Google Colab (Free)
1. Go to [Google Colab](https://colab.research.google.com/)
2. Sign in with your Google account
3. Click "New Notebook" to start coding immediately

**Try it now**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/leekwansoo/python-excercise/blob/main/_0environment_setup.ipynb)

### 🔬 Binder (Free)
1. Click any "Launch Binder" badge in our course materials
2. Wait for the environment to load (2-3 minutes)
3. Start coding in a full Jupyter Lab environment

**Try it now**: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/leekwansoo/python-excercise/main?labpath=_0environment_setup.ipynb)

---

## 💻 Option 2: Local Installation (Recommended for Serious Learning)

**Perfect for**: Long-term learning, offline access, professional development

### Why Local Installation?
- 🏃‍♂️ Faster execution and response times
- 🔒 Complete privacy and control over your code
- 📱 Offline access to all materials
- 🛠️ Access to advanced development tools
- 💼 Professional development workflow experience

## Step-by-Step Local Setup

### Step 1: Install Python

#### For Windows:
1. **Download Python**
   - Visit [python.org](https://www.python.org/downloads/)
   - Download Python 3.12 or later
   - **Important**: Check "Add Python to PATH" during installation

2. **Verify Installation**
   ```cmd
   python --version
   pip --version
   ```

#### For macOS:
1. **Using Homebrew** (Recommended)
   ```bash
   # Install Homebrew if you haven't already
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   
   # Install Python
   brew install python
   ```

2. **Direct Download**
   - Visit [python.org](https://www.python.org/downloads/)
   - Download the macOS installer
   - Run the installer and follow instructions

#### For Linux (Ubuntu/Debian):
```bash
# Update package list
sudo apt update

# Install Python 3 and pip
sudo apt install python3 python3-pip

# Verify installation
python3 --version
pip3 --version
```

### Step 2: Install Jupyter Lab

Jupyter Lab is the modern interface for interactive Python programming:

```bash
# Install Jupyter Lab
pip install jupyterlab

# Install additional useful packages
pip install numpy pandas matplotlib seaborn requests
```

### Step 3: Download Course Materials

```bash
# Clone the course repository
git clone https://github.com/leekwansoo/python-excercise.git

# Navigate to the course folder
cd python-excercise

# Install course requirements
pip install -r requirements.txt
```

### Step 4: Launch Jupyter Lab

```bash
# Start Jupyter Lab
jupyter lab

# Your browser will open automatically at http://localhost:8888
```

---

## 🎯 Option 3: Anaconda Distribution (All-in-One Solution)

**Perfect for**: Data science focus, comprehensive package management

### What is Anaconda?
Anaconda is a complete Python distribution that includes:
- Python interpreter
- Jupyter Lab and Notebook
- 250+ pre-installed scientific packages
- Conda package manager
- Spyder IDE

### Installation Steps:
1. **Download Anaconda**
   - Visit [anaconda.com](https://www.anaconda.com/products/distribution)
   - Choose your operating system
   - Download the installer (3+ GB)

2. **Install Anaconda**
   - Run the installer
   - Accept default settings
   - Installation takes 10-20 minutes

3. **Launch Anaconda Navigator**
   - Find Anaconda Navigator in your applications
   - Launch Jupyter Lab from the interface
   - Start coding immediately!

### Managing Environments with Conda:
```bash
# Create a new environment for this course
conda create --name python-course python=3.12

# Activate the environment
conda activate python-course

# Install additional packages
conda install pandas matplotlib seaborn
```

---

## 🧪 Testing Your Setup

Let's verify everything is working correctly:

### Test 1: Basic Python
```python
print("Hello, Python World! 🐍")
print(f"Python is working correctly!")
```

### Test 2: Import Essential Libraries
```python
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print(f"Python version: {sys.version}")
print("✅ All essential libraries imported successfully!")
```

### Test 3: Create Your First Plot
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label='sin(x)')
plt.title('Your First Python Plot! 📊')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print("🎉 Congratulations! Your Python environment is ready!")
```

---

## 🎯 Interactive Setup Verification

Ready to test your setup interactively?

[![Test Your Setup](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/leekwansoo/python-excercise/main?labpath=_0environment_setup.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/leekwansoo/python-excercise/blob/main/_0environment_setup.ipynb)

---

## 🆘 Troubleshooting Common Issues

### Issue: "python" command not found
**Solution**: 
- Windows: Reinstall Python and check "Add to PATH"
- macOS/Linux: Use `python3` instead of `python`

### Issue: Permission errors when installing packages
**Solution**:
```bash
# Use --user flag to install for current user only
pip install --user package_name

# Or use virtual environments (recommended)
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
pip install package_name
```

### Issue: Jupyter Lab won't start
**Solution**:
```bash
# Try upgrading Jupyter
pip install --upgrade jupyterlab

# Clear browser cache and try again
# Check if port 8888 is in use
jupyter lab --port=8889
```

---

## ✅ Setup Checklist

Before moving to the next lesson, ensure you have:

- [ ] Python 3.8+ installed and working
- [ ] Pip package manager available
- [ ] Jupyter Lab or Notebook interface accessible
- [ ] Course materials downloaded/accessible
- [ ] Successfully run the test code snippets above

## 🎉 You're Ready!

Congratulations! You now have a fully functional Python development environment. You're ready to begin your Python programming journey!

**Next Step**: [Your First Python Program](../02-basics/getting-started.md)

---

**💡 Pro Tips**:
- Bookmark your Jupyter Lab URL for quick access
- Create a dedicated folder for your Python projects
- Join Python communities online for continued learning and support
- Practice coding a little bit every day for best results