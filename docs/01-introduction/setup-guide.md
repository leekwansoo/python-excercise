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
   - Visit [python.org](https://www.python.org/downloads/) from your Browser
   - Download Python 3.12 or later release
   - **Important**: Check "Add Python to PATH" during installation

2. **Verify Installation from cmd window**
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

### Step 2: Install Visual Studio Code

1. **Direct Download**
   - Visit [code.visualstudio.com](https://code.visualstudio.com/download)
   - Download Visual Studio Code installer for Windows
   - Run the installer and follow instructions
   - VS Code is the most popular Integrated Development Tool

### Step 3: Set Up Git Bash Terminal in VS Code 🔧

**Why Git Bash?** Git Bash provides a Unix-like command-line environment on Windows, allowing you to use Git commands and bash scripts seamlessly.

#### **3.1: Install Git for Windows (Includes Git Bash)**

1. **Download Git for Windows**
   - Visit [git-scm.com/download/win](https://git-scm.com/download/win)
   - Download the latest version (usually auto-downloads)

2. **Installation Process** (Important Settings!)
   - Run the downloaded installer
   - **Select Components**: ✅ Check "Git Bash Here"
   - **Default Editor**: Choose "Use Visual Studio Code as Git's default editor"
   - **PATH Environment**: Select "Git from the command line and also from 3rd-party software"
   - **Line Ending**: Select "Checkout Windows-style, commit Unix-style line endings"
   - **Terminal Emulator**: Select "Use Windows' default console window"
   - **Accept all other default settings**

#### **3.2: Configure Git Bash in VS Code Terminal**

1. **Open VS Code**

2. **Open Terminal Settings**
   - Press `Ctrl + Shift + P` to open Command Palette
   - Type "Terminal: Select Default Profile"
   - Press Enter

3. **Add Git Bash Profile** (if not automatically detected)
   - Press `Ctrl + Shift + P`
   - Type "Preferences: Open Settings (JSON)"
   - Add this configuration:

   ```json
   {
       "terminal.integrated.profiles.windows": {
           "PowerShell": {
               "source": "PowerShell",
               "icon": "terminal-powershell"
           },
           "Command Prompt": {
               "path": [
                   "${env:windir}\\Sysnative\\cmd.exe",
                   "${env:windir}\\System32\\cmd.exe"
               ],
               "args": [],
               "icon": "terminal-cmd"
           },
           "Git Bash": {
               "path": "C:\\Program Files\\Git\\bin\\bash.exe",
               "args": [],
               "icon": "terminal-bash"
           }
       },
       "terminal.integrated.defaultProfile.windows": "Git Bash"
   }
   ```

4. **Alternative Method - Automatic Detection**
   - Open VS Code
   - Press `Ctrl + Shift + ` (backtick) to open terminal
   - Click the dropdown arrow next to the `+` in terminal tab
   - Select "Git Bash" from the list

#### **3.3: Verify Git Bash Installation**

1. **Open New Terminal in VS Code**
   - Press `Ctrl + Shift + ` (backtick)
   - You should see "bash" in the terminal tab

2. **Test Commands**
   ```bash
   # Check Git version
   git --version
   
   # Check current directory
   pwd
   
   # List files
   ls -la
   
   # Check Python version
   python --version
   ```

#### **3.4: Set Git Configuration** (First Time Setup)

In the Git Bash terminal, configure your Git identity:

```bash
# Set your name (replace with your actual name)
git config --global user.name "Your Name"

# Set your email (replace with your actual email)
git config --global user.email "your.email@example.com"

# Verify configuration
git config --list
```

#### **3.5: Terminal Selection in VS Code**

Now you can easily switch between terminals:

1. **Open Terminal**: `Ctrl + Shift + ` (backtick)
2. **Create New Terminal**: Click the `+` dropdown
3. **Select Terminal Type**:
   - **Git Bash** (for Git commands and Unix-like experience)
   - **PowerShell** (for Windows commands)
   - **Command Prompt** (for traditional Windows commands)

### Step 4: Download Course Materials

```bash
# Clone the course repository
git clone https://github.com/leekwansoo/python-excercise.git

# Navigate to the course folder
cd python-excercise

# Install course requirements
pip install -r requirements.txt
```

## 🎯 Visual Guide: VS Code Terminal Setup

### **What Students Should See:**

#### **Terminal Selection Dropdown:**
When students click the dropdown next to `+` in the terminal, they should see:
- ✅ **Git Bash** ← This is what we want!
- PowerShell
- Command Prompt

#### **Git Bash Terminal Features:**
```bash
# Students will see this prompt in Git Bash:
MINGW64 /c/Users/YourName/Desktop/python-excercise-main (main)
$ 

# They can use Unix-like commands:
$ ls -la          # List files (instead of 'dir')
$ pwd             # Show current directory
$ cd session_01   # Change directory
$ git status      # Check Git repository status
$ python app.py   # Run Python files
```

## 🛠️ Troubleshooting Common Issues

### **Issue 1: Git Bash Not Appearing in VS Code**

**Solution:**
1. **Restart VS Code** after installing Git
2. **Manually add the path**:
   - Press `Ctrl + ,` (Settings)
   - Search for "terminal profiles"
   - Click "Edit in settings.json"
   - Add the Git Bash profile manually (see JSON above)

### **Issue 2: "bash: command not found"**

**Solution:**
```bash
# Check if Git is properly installed
where git

# If not found, reinstall Git for Windows
# Make sure to select "Add Git to PATH" during installation
```

### **Issue 3: Permission Denied Errors**

**Solution:**
```bash
# Run VS Code as Administrator (right-click VS Code icon)
# Or check file permissions:
ls -la filename.txt
```

#### **Issue 4: Git Commands Not Working**

**Verify Git Installation:**
```bash
# These commands should work in Git Bash:
git --version    # Should show Git version
which git        # Should show Git path
echo $PATH       # Should includes Git paths
```

## 📚 Essential Git Bash Commands for Students

### **File and Directory Operations:**
```bash
# List files and directories
ls                 # Basic listing
ls -la            # Detailed listing with hidden files
ls -lh            # Human-readable file sizes

# Navigate directories
pwd               # Print working directory
cd directory_name # Change to directory
cd ..             # Go up one directory
cd ~              # Go to home directory
cd /c/Users/      # Navigate to Windows Users folder
```

### **Git Operations:**
```bash
# Check repository status
git status

# Clone a repository
git clone https://github.com/username/repository.git

# Add files to staging
git add filename.txt    # Add specific file
git add .              # Add all files

# Commit changes
git commit -m "Your commit message"

# Push to remote repository
git push origin main
```

### **Python Operations:**
```bash
# Run Python files
python filename.py
python app.py

# Install packages
pip install package_name
pip install -r requirements.txt

# Check Python version
python --version
pip --version
```

## 🎓 Class Instructions Template

### **For Instructors - What to Tell Students:**

> **"Today we'll set up Git Bash in VS Code so you can use powerful Unix commands and Git version control."**

**Step-by-Step for Students:**

1. **"Open VS Code"**
2. **"Press Ctrl + Shift + ` (the key above Tab) to open terminal"**
3. **"Click the small dropdown arrow next to the + sign"**
4. **"If you see 'Git Bash' - select it!"**
5. **"If you don't see it, raise your hand for help"**

**What Success Looks Like:**
- Terminal shows: `MINGW64` in the prompt
- Commands like `ls`, `pwd`, `git status` work
- Can navigate using Unix-style paths

**Common Student Questions:**
- **Q:** "Why not just use PowerShell?"
- **A:** "Git Bash gives us Unix commands that work the same on Mac/Linux, and better Git integration"

- **Q:** "What's the difference between the terminals?"
- **A:** "Think of them as different languages - PowerShell speaks Windows, Git Bash speaks Unix/Linux"

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
