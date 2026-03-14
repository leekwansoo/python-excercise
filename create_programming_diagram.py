import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(16, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Define colors
input_color = '#e1f5fe'
process_color = '#f3e5f5'
output_color = '#e8f5e8'
env_color = '#fff3e0'

# OS Environment (top layer)
env_box = FancyBboxPatch((0.5, 8.5), 9, 1.2, boxstyle="round,pad=0.1", 
                         facecolor=env_color, edgecolor='#e65100', linewidth=2)
ax.add_patch(env_box)
ax.text(5, 9.1, 'OS Environment', ha='center', va='center', fontsize=14, fontweight='bold')
ax.text(2.5, 8.8, 'Operating System\nWindows/Linux/macOS\nFile System, Memory', ha='center', va='center', fontsize=9)
ax.text(7.5, 8.8, 'Python Runtime\nInterpreter, Virtual Env\nInstalled Packages', ha='center', va='center', fontsize=9)

# Input Variables (left side)
input_boxes = [
    (0.5, 6.5, 'User Input\nname = "John"\nage = 25'),
    (0.5, 5.5, 'File Data\ndata.csv\nconfig.json'),
    (0.5, 4.5, 'API Data\nweather_data\nuser_info'),
    (0.5, 3.5, 'Configuration\nsettings.json\nparameters')
]

for x, y, text in input_boxes:
    box = FancyBboxPatch((x, y), 2, 0.8, boxstyle="round,pad=0.05", 
                         facecolor=input_color, edgecolor='#01579b', linewidth=2)
    ax.add_patch(box)
    ax.text(x+1, y+0.4, text, ha='center', va='center', fontsize=8)

# Processing Layer (center)
# Operators
ops_box = FancyBboxPatch((3, 6.5), 2, 1.5, boxstyle="round,pad=0.05", 
                         facecolor=process_color, edgecolor='#4a148c', linewidth=2)
ax.add_patch(ops_box)
ax.text(4, 7.6, 'Operators', ha='center', va='center', fontsize=10, fontweight='bold')
ax.text(4, 7.2, 'Arithmetic: + - * /', ha='center', va='center', fontsize=8)
ax.text(4, 6.9, 'Comparison: == != < >', ha='center', va='center', fontsize=8)
ax.text(4, 6.6, 'Logical: and or not', ha='center', va='center', fontsize=8)

# Built-in Functions
builtin_box = FancyBboxPatch((3, 4.8), 2, 1.2, boxstyle="round,pad=0.05", 
                            facecolor=process_color, edgecolor='#4a148c', linewidth=2)
ax.add_patch(builtin_box)
ax.text(4, 5.7, 'Built-in Functions', ha='center', va='center', fontsize=10, fontweight='bold')
ax.text(4, 5.3, 'len(), print(), type()', ha='center', va='center', fontsize=8)
ax.text(4, 5.0, 'str(), int(), float()', ha='center', va='center', fontsize=8)

# Modules
modules_box = FancyBboxPatch((3, 3), 2, 1.5, boxstyle="round,pad=0.05", 
                            facecolor=process_color, edgecolor='#4a148c', linewidth=2)
ax.add_patch(modules_box)
ax.text(4, 4.1, 'Modules & Libraries', ha='center', va='center', fontsize=10, fontweight='bold')
ax.text(4, 3.7, 'Standard: os, sys, math', ha='center', va='center', fontsize=8)
ax.text(4, 3.4, 'External: pandas, numpy', ha='center', va='center', fontsize=8)
ax.text(4, 3.1, 'Custom Functions', ha='center', va='center', fontsize=8)

# Output Results (right side)
output_boxes = [
    (7.5, 6.5, 'Console Output\nprint statements\nerror messages'),
    (7.5, 5.5, 'File Output\nresults.txt\nreport.csv'),
    (7.5, 4.5, 'Web Output\nHTML pages\nAPI responses'),
    (7.5, 3.5, 'Visualizations\nCharts & Graphs\nPlots')
]

for x, y, text in output_boxes:
    box = FancyBboxPatch((x, y), 2, 0.8, boxstyle="round,pad=0.05", 
                         facecolor=output_color, edgecolor='#1b5e20', linewidth=2)
    ax.add_patch(box)
    ax.text(x+1, y+0.4, text, ha='center', va='center', fontsize=8)

# Add arrows for data flow
# Input to Processing
arrow_props = dict(arrowstyle='->', lw=2, color='#666666')

# Input arrows
for i, (_, y, _) in enumerate(input_boxes):
    ax.annotate('', xy=(3, y+0.4), xytext=(2.5, y+0.4), arrowprops=arrow_props)

# Processing to Output arrows
for i, (_, y, _) in enumerate(output_boxes):
    ax.annotate('', xy=(7.5, y+0.4), xytext=(5, 5.5), arrowprops=arrow_props)

# Environment arrows (dotted)
env_arrow_props = dict(arrowstyle='->', lw=1, color='#999999', linestyle='--')
ax.annotate('', xy=(4, 6.5), xytext=(5, 8.5), arrowprops=env_arrow_props)

# Add title
ax.text(5, 9.7, 'Programming Process Flow Diagram', ha='center', va='center', 
        fontsize=16, fontweight='bold')

# Add legend
legend_x = 0.5
legend_y = 2
ax.text(legend_x, legend_y, 'Legend:', fontsize=10, fontweight='bold')

legend_items = [
    (input_color, 'Input Variables'),
    (process_color, 'Processing Layer'),
    (output_color, 'Output Results'),
    (env_color, 'OS Environment')
]

for i, (color, label) in enumerate(legend_items):
    y_pos = legend_y - 0.3 - (i * 0.3)
    legend_box = FancyBboxPatch((legend_x, y_pos), 0.3, 0.2, boxstyle="round,pad=0.02", 
                               facecolor=color, edgecolor='black', linewidth=1)
    ax.add_patch(legend_box)
    ax.text(legend_x + 0.4, y_pos + 0.1, label, ha='left', va='center', fontsize=9)

# Save the figure
plt.tight_layout()
plt.savefig('programming_process_diagram.jpg', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.savefig('programming_process_diagram.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')

print("Diagram saved as 'programming_process_diagram.jpg' and 'programming_process_diagram.png'")
plt.show()