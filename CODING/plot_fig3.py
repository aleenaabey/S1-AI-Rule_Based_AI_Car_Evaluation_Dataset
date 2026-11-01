# Student Name: Aleena Abey
# CPU5006: Artificial Intelligence - Assessment 1
# File: plot_fig3_performance.py
# Purpose: Generates Figure 3 (Overall Metrics Comparison Bar Chart)
# Note: Matplotlib code assisted by AI tool as permitted by module brief.

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
expert_system = [78.4, 74.1, 76.8, 75.4]
cba_algorithm = [88.6, 86.5, 87.1, 86.8]

x = np.arange(len(metrics))
width = 0.35

fig, ax = plt.subplots(figsize=(6.5, 4.0))
b1 = ax.bar(x - width/2, expert_system, width, label='Algorithm 1 (Expert System)', color='#2B5B84', edgecolor='black')
b2 = ax.bar(x + width/2, cba_algorithm, width, label='Algorithm 2 (Inductive CBA)', color='#E07A5F', edgecolor='black')

ax.set_title('Figure 3: Overall Classification Performance Comparison', fontsize=11, fontweight='bold', pad=10)
ax.set_ylabel('Score (%)', fontsize=10, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(metrics, fontsize=10)
ax.set_ylim(0, 105)
ax.legend(loc='lower right', frameon=True)
ax.grid(axis='y', linestyle='--', alpha=0.6)

for bar in b1:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1.2, f"{yval:.1f}%", ha='center', va='bottom', fontsize=8.5)

for bar in b2:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1.2, f"{yval:.1f}%", ha='center', va='bottom', fontsize=8.5)

plt.tight_layout()
plt.savefig('Figure_3_Performance_Comparison.png', dpi=300)
print("Saved: Figure_3_Performance_Comparison.png")
plt.show()