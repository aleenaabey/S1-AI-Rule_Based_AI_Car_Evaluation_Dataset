# Student Name: Aleena Abey
# CPU5006: Artificial Intelligence - Assessment 1
# Generating Figure 1 (Class Distribution) and Figure 3 (Confusion Matrices)
# Note: Matplotlib code assisted by AI tool as permitted by module brief.

import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------------------------------------
# 1. FIGURE 1: CLASS DISTRIBUTION BAR CHART (For Methodology Section)
# ------------------------------------------------------------------------------
classes = ['unacc', 'acc', 'good', 'vgood']
counts = [1210, 384, 69, 65]
percentages = [70.02, 22.22, 3.99, 3.76]

fig1, ax1 = plt.subplots(figsize=(6.5, 4.2))
colors = ['#c0392b', '#2980b9', '#27ae60', '#f39c12']

bars = ax1.bar(classes, counts, color=colors, edgecolor='black', width=0.55)
ax1.set_title('Figure 1: Class Distribution of the Car Evaluation Dataset (N=1,728)', fontsize=11, fontweight='bold', pad=12)
ax1.set_xlabel('Vehicle Acceptability Class', fontsize=10, fontweight='bold')
ax1.set_ylabel('Number of Instances', fontsize=10, fontweight='bold')
ax1.set_ylim(0, 1400)
ax1.grid(axis='y', linestyle='--', alpha=0.6)

# Add exact counts and percentages above each bar
for bar, pct in zip(bars, percentages):
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 25, f"{int(yval)}\n({pct:.1f}%)", ha='center', va='bottom', fontsize=8.5)

plt.tight_layout()
plt.savefig('figure1_class_distribution.png', dpi=300)
print("--> Saved: figure1_class_distribution.png")
plt.close(fig1)

# ------------------------------------------------------------------------------
# 2. FIGURE 3: CONFUSION MATRICES HEATMAP (For Results Section)
# Shows exactly which classes were predicted vs actual on test data (N=519)
# ------------------------------------------------------------------------------
# Matrix format: rows = Actual, cols = Predicted [unacc, acc, good, vgood]
cm_expert = np.array([
    [321,  30,   7,   5],  # Actual unacc
    [ 20,  78,  10,   7],  # Actual acc
    [  0,   3,  15,   3],  # Actual good
    [  0,   1,   3,  16]   # Actual vgood
])

cm_cba = np.array([
    [346,  12,   3,   2],  # Actual unacc
    [ 11,  91,   7,   6],  # Actual acc
    [  0,   2,  18,   1],  # Actual good
    [  0,   1,   1,  18]   # Actual vgood
])

fig3, (ax_e, ax_c) = plt.subplots(1, 2, figsize=(11, 4.8))

for ax, cm, title in zip([ax_e, ax_c], [cm_expert, cm_cba], 
                        ['Algorithm 1: Deductive Expert', 'Algorithm 2: Inductive CBA']):
    im = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    ax.set_title(title, fontsize=10, fontweight='bold', pad=10)
    tick_marks = np.arange(len(classes))
    ax.set_xticks(tick_marks)
    ax.set_yticks(tick_marks)
    ax.set_xticklabels(classes, fontsize=9)
    ax.set_yticklabels(classes, fontsize=9)
    ax.set_xlabel('Predicted Label', fontsize=9, fontweight='bold')
    ax.set_ylabel('True (Actual) Label', fontsize=9, fontweight='bold')

    # Print numbers inside each heatmap square
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], 'd'),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black",
                    fontsize=9.5)

fig3.suptitle('Figure 3: Test Set Confusion Matrices (N=519 Holdout Instances)', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('figure3_confusion_matrices.png', dpi=300)
print("--> Saved: figure3_confusion_matrices.png")
plt.close(fig3)

print("\nFinished! Both Figure 1 and Figure 3 have been generated.")