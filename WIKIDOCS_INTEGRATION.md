# Wikidocs Integration Guide

## How to Integrate Jupyter Notebooks with Wikidocs

### Method 1: Link to Interactive Notebooks

In your wikidocs pages, add buttons that link to executable versions:

```markdown
## Python Math Module Exercise

📖 **Read the theory** in this wiki page, then **practice with code**:

[🚀 **Practice Interactive Notebook**](https://mybinder.org/v2/gh/leekwansoo/python-excercise/main?labpath=python_math_module.ipynb)

[📱 **Open in Google Colab**](https://colab.research.google.com/github/leekwansoo/python-excercise/blob/main/python_math_module.ipynb)
```

### Method 2: Embed Static Content

Convert notebooks to markdown and paste in wikidocs:

```bash
# Convert to markdown
jupyter nbconvert --to markdown python_math_module.ipynb

# Copy the content from .md file to your wiki
```

### Method 3: Embed HTML Preview

```html
<iframe src="https://github.com/leekwansoo/python-excercise/blob/main/python_math_module.ipynb" 
        width="100%" height="600px" frameborder="0">
</iframe>
```

### Method 4: Screenshots + Links

1. Take screenshots of key notebook sections
2. Add them to wikidocs with explanations
3. Link to the executable version for hands-on practice

## Recommended Workflow

### In Wikidocs:
- **Concepts & Theory**: Write explanations, definitions, examples
- **Visual Learning**: Add diagrams, flowcharts, concept maps
- **Assessment**: Quizzes, questions, exercises descriptions

### In GitHub Notebooks:
- **Hands-on Practice**: Interactive code execution
- **Real Examples**: Working code with output
- **Experimentation**: Students can modify and test code

### Integration Points:

```markdown
## Variables in Python

Variables are containers for storing data values...

### 🎯 **Practice Time!**
Now that you understand the concept, let's practice with real code:

[📝 **Interactive Variables Exercise**](https://mybinder.org/v2/gh/leekwansoo/python-excercise/main?labpath=_1variables.ipynb)

**What you'll do:**
- Create your first variables
- Learn naming conventions  
- Practice different data assignments
- See real Python output

[▶️ **Start Exercise**](https://mybinder.org/v2/gh/leekwansoo/python-excercise/main?labpath=_1variables.ipynb)
```

## Benefits of This Approach

✅ **Best of Both Worlds**: Theory in wikidocs + Practice in notebooks  
✅ **No Installation Required**: Students use browser-based environments  
✅ **Always Updated**: Links point to your latest GitHub version  
✅ **Progressive Learning**: Read → Understand → Practice → Apply  
✅ **Accessible**: Works on any device with internet  

## Student Experience

1. **Read concept** in wikidocs with rich formatting and explanations
2. **Click practice link** to open interactive notebook
3. **Run and modify code** to reinforce learning
4. **Return to wiki** for next concept or assessment

This creates a seamless learning experience! 🎓