# Student Name: Aleena Abey
# CPU5006: Artificial Intelligence - Assessment 1
# Plotting Experimental Figures for Rule-Based AI Evaluation
# Note: Matplotlib code assisted by AI tool as permitted by module brief.

import matplotlib.pyplot as plt
import numpy as np

# Apply a clean academic styling
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

# ------------------------------------------------------------------------------
# FIGURE 1: OVERALL CLASSIFICATION PERFORMANCE METRICS
# (Insert into Section 4.1 of Results)
# ------------------------------------------------------------------------------
metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
expert_system = [78.4, 74.1, 76.8, 75.4]
cba_algorithm = [88.6, 86.5, 87.1, 86.8]

x1 = np.arange(len(metrics))
width = 0.35

fig1, ax1 = plt.subplots(figsize=(6.5, 4.2))

# Color palette: Classic Navy and Dark Teal for clean academic print
b1 = ax1.bar(x1 - width/2, expert_system, width, label='Algorithm 1 (Expert System)', color="#7B1F46", edgecolor='black')
b2 = ax1.bar(x1 + width/2, cba_algorithm, width, label='Algorithm 2 (CBA Induction)', color="#7B326B", edgecolor='black')

ax1.set_title('Figure 1: Overall Classification Performance Comparison', fontsize=11, fontweight='bold', pad=12)
ax1.set_ylabel('Score (%)', fontsize=10, fontweight='bold')
ax1.set_xticks(x1)
ax1.set_xticklabels(metrics, fontsize=10)
ax1.set_ylim(0, 105)
ax1.legend(loc='lower right', frameon=True)
ax1.grid(axis='y', linestyle='--', alpha=0.6)

# Add exact value labels on top of each bar
for bar in b1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 1.2, f"{yval:.1f}%", ha='center', va='bottom', fontsize=8.5)

for bar in b2:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 1.2, f"{yval:.1f}%", ha='center', va='bottom', fontsize=8.5)

plt.tight_layout()
plt.savefig('figure1_metrics_comparison.png', dpi=300)
print("--> Successfully saved: figure1_metrics_comparison.png")
plt.close(fig1)

# ------------------------------------------------------------------------------
# FIGURE 2: SAFETY VETO CONSTRAINT HANDLING
# (Insert into Section 4.3 of Results)
# ------------------------------------------------------------------------------
categories = ['Correctly Rejected\n(Unacc)', 'Misclassified\n(Acc)']
algo1_veto = [174, 0]
algo2_veto = [169, 5]

x2 = np.arange(len(categories))

fig2, ax2 = plt.subplots(figsize=(6, 4.2))

b3 = ax2.bar(x2 - width/2, algo1_veto, width, label='Algorithm 1 (Expert)', color="#765EA0", edgecolor='black')
b4 = ax2.bar(x2 + width/2, algo2_veto, width, label='Algorithm 2 (CBA)', color="#1E7B8C", edgecolor='black')

ax2.set_title('Figure 2: Non-Compensatory Safety Veto Handling (N=174)', fontsize=11, fontweight='bold', pad=12)
ax2.set_ylabel('Number of Low-Safety Cars', fontsize=10, fontweight='bold')
ax2.set_xticks(x2)
ax2.set_xticklabels(categories, fontsize=10)
ax2.set_ylim(0, 200)
ax2.legend(loc='upper right', frameon=True)
ax2.grid(axis='y', linestyle='--', alpha=0.6)

# Add exact count numbers on top of each bar
for bar in b3:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 2.5, f"{int(yval)}", ha='center', va='bottom', fontsize=9)

for bar in b4:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 2.5, f"{int(yval)}", ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('figure2_safety_veto.png', dpi=300)
print("--> Successfully saved: figure2_safety_veto.png")
plt.close(fig2)

print("\nAll done! Check your folder for the two separate PNG files.")