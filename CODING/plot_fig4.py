# Student Name: Aleena Abey
# CPU5006: Artificial Intelligence - Assessment 1
# File: plot_fig4_confusion.py
# Purpose: Generates Figure 4 (Side-by-Side Confusion Matrices)
# Note: Matplotlib code assisted by AI tool as permitted by module brief.

import matplotlib.pyplot as plt
import numpy as np

classes = ['unacc', 'acc', 'good', 'vgood']

cm_expert = np.array([
    [321,  30,   7,   5],
    [ 20,  78,  10,   7],
    [  0,   3,  15,   3],
    [  0,   1,   3,  16]
])

cm_cba = np.array([
    [346,  12,   3,   2],
    [ 11,  91,   7,   6],
    [  0,   2,  18,   1],
    [  0,   1,   1,  18]
])

fig, (ax_e, ax_c) = plt.subplots(1, 2, figsize=(10.5, 4.5))

for ax, cm, title in zip([ax_e, ax_c], [cm_expert, cm_cba], 
                        ['Algorithm 1: Deductive Expert', 'Algorithm 2: Inductive CBA']):
    ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    ax.set_title(title, fontsize=10, fontweight='bold', pad=10)
    tick_marks = np.arange(len(classes))
    ax.set_xticks(tick_marks)
    ax.set_yticks(tick_marks)
    ax.set_xticklabels(classes, fontsize=9)
    ax.set_yticklabels(classes, fontsize=9)
    ax.set_xlabel('Predicted Label', fontsize=9, fontweight='bold')
    ax.set_ylabel('True (Actual) Label', fontsize=9, fontweight='bold')

    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], 'd'),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black",
                    fontsize=9.5)

fig.suptitle('Figure 4: Test Set Confusion Matrices (N=519 Holdout Instances)', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('Figure_4_Confusion_Matrices.png', dpi=300)
print("Saved: Figure_4_Confusion_Matrices.png")
plt.show()