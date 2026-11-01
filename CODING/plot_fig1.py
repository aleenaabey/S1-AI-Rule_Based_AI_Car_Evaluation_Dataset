# Student Name: Aleena Abey
# CPU5006: Artificial Intelligence - Assessment 1
# File: plot_fig1_distribution.py
# Purpose: Generates Figure 1 (Class Distribution Bar Chart)
# Note: Matplotlib code assisted by AI tool as permitted by module brief.

import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

classes = ['unacc', 'acc', 'good', 'vgood']
counts = [1210, 384, 69, 65]
percentages = [70.02, 22.22, 3.99, 3.76]
colors = ['#c0392b', '#2980b9', '#27ae60', '#f39c12']

fig, ax = plt.subplots(figsize=(6.5, 4.0))
bars = ax.bar(classes, counts, color=colors, edgecolor='black', width=0.55)

ax.set_title('Figure 1: Class Distribution of the Car Evaluation Dataset (N=1,728)', fontsize=11, fontweight='bold', pad=10)
ax.set_xlabel('Vehicle Acceptability Class', fontsize=10, fontweight='bold')
ax.set_ylabel('Number of Instances', fontsize=10, fontweight='bold')
ax.set_ylim(0, 1400)
ax.grid(axis='y', linestyle='--', alpha=0.6)

# Add exact numbers and percentages on top of each bar
for bar, pct in zip(bars, percentages):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 25, f"{int(yval)}\n({pct:.1f}%)", ha='center', va='bottom', fontsize=8.5)

plt.tight_layout()
plt.savefig('Figure_1_Class_Distribution.png', dpi=300)
print("Saved: Figure_1_Class_Distribution.png")
plt.show()