# Student Name: Aleena Abey
# CPU5006: Artificial Intelligence - Assessment 1
# File: plot_fig2_architecture.py
# Purpose: Generates Figure 2 (System Architecture Diagram)
# Note: Diagram layout assisted by AI tool as permitted by module brief.

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8.5, 4.2))
ax.axis('off')

# Box styles
box_input = dict(boxstyle='round,pad=0.5', facecolor='#FCF3CF', edgecolor='#B7950B', linewidth=1.5)
box_algo1 = dict(boxstyle='round,pad=0.5', facecolor='#D4E6F1', edgecolor='#2471A3', linewidth=1.5)
box_algo2 = dict(boxstyle='round,pad=0.5', facecolor='#E8DAEF', edgecolor='#7D3C98', linewidth=1.5)
box_output = dict(boxstyle='round,pad=0.5', facecolor='#D5F5E3', edgecolor='#229954', linewidth=1.5)

# Text nodes
ax.text(0.12, 0.5, "Input Instance:\n(6 Features)\nbuying, maint,\ndoors, persons,\nlug_boot, safety", 
        ha='center', va='center', fontsize=9, bbox=box_input)

ax.text(0.50, 0.78, "Algorithm 1: Deductive Expert Hierarchy\n- Modular Tables: PRICE, COMFORT, TECH\n- Enforces Mandatory Safety Veto", 
        ha='center', va='center', fontsize=8.5, bbox=box_algo1)

ax.text(0.50, 0.22, "Algorithm 2: Inductive Rule Learner (CBA)\n- Propositional Separate-and-Conquer Rules\n- Precedence: Confidence -> Support -> Length", 
        ha='center', va='center', fontsize=8.5, bbox=box_algo2)

ax.text(0.88, 0.5, "Predicted Class:\nunacc / acc\ngood / vgood", 
        ha='center', va='center', fontsize=9, fontweight='bold', bbox=box_output)

# Connecting arrows
arrow = dict(arrowstyle='->', lw=1.5, color='#34495E')
ax.annotate('', xy=(0.30, 0.78), xytext=(0.22, 0.55), arrowprops=arrow)
ax.annotate('', xy=(0.30, 0.22), xytext=(0.22, 0.45), arrowprops=arrow)
ax.annotate('', xy=(0.80, 0.55), xytext=(0.70, 0.78), arrowprops=arrow)
ax.annotate('', xy=(0.80, 0.45), xytext=(0.70, 0.22), arrowprops=arrow)

plt.title('Figure 2: System Architecture of Deductive vs Inductive Rule-Based AI', fontsize=11, fontweight='bold', pad=12)
plt.tight_layout()
plt.savefig('Figure_2_System_Architecture.png', dpi=300)
print("Saved: Figure_2_System_Architecture.png")
plt.show()