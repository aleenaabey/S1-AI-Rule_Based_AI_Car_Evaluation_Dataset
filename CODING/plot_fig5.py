# Student Name: Aleena Abey
# CPU5006: Artificial Intelligence - Assessment 1
# File: plot_fig5_sensitivity.py
# Purpose: Generates Figure 5 (Parameter Sensitivity Line Graph)
# Note: Matplotlib code assisted by AI tool as permitted by module brief.

import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

confidence_thresholds = [50, 60, 70, 80, 90]
accuracy_trend = [79.2, 83.5, 88.6, 85.1, 78.0]
rule_count_trend = [34, 28, 19, 14, 8]

fig, ax_line = plt.subplots(figsize=(6.5, 4.0))

# Line 1: Accuracy (Blue)
color1 = '#1f77b4'
ax_line.set_xlabel('Minimum Rule Confidence Threshold (%)', fontsize=10, fontweight='bold')
ax_line.set_ylabel('Overall Accuracy (%)', color=color1, fontsize=10, fontweight='bold')
line1 = ax_line.plot(confidence_thresholds, accuracy_trend, marker='o', linewidth=2.5, color=color1, label='Accuracy (%)')
ax_line.tick_params(axis='y', labelcolor=color1)
ax_line.set_ylim(65, 100)

# Line 2: Rule Count (Orange)
ax_twin = ax_line.twinx()
color2 = '#ff7f0e'
ax_twin.set_ylabel('Total Mined Rules (Compactness)', color=color2, fontsize=10, fontweight='bold')
line2 = ax_twin.plot(confidence_thresholds, rule_count_trend, marker='s', linestyle='--', linewidth=2, color=color2, label='Rule Count')
ax_twin.tick_params(axis='y', labelcolor=color2)
ax_twin.set_ylim(0, 45)

plt.title('Figure 5: Algorithm 2 Parameter Sensitivity & Rule Pruning Trend', fontsize=11, fontweight='bold', pad=10)
ax_line.grid(True, linestyle='--', alpha=0.5)

lines = line1 + line2
labels = [l.get_label() for l in lines]
ax_line.legend(lines, labels, loc='lower left', frameon=True)

plt.tight_layout()
plt.savefig('Figure_5_Parameter_Sensitivity.png', dpi=300)
print("Saved: Figure_5_Parameter_Sensitivity.png")
plt.show()