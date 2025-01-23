
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow, Rectangle, Circle

# Initialize figure
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Draw skeletal muscle
muscle = Rectangle((1, 8), 2, 1, edgecolor='black', facecolor='lightblue', lw=2)
ax.add_patch(muscle)
ax.text(2, 8.5, 'Skeletal Muscle', ha='center', fontsize=10)

# Arrow to Metrnl release
arrow1 = FancyArrow(3, 8.5, 2, 0, width=0.2, color='black')
ax.add_patch(arrow1)

# Draw Metrnl release
metrnl = Circle((6, 8.5), 0.6, edgecolor='black', facecolor='lightgreen', lw=2)
ax.add_patch(metrnl)
ax.text(6, 8.5, 'Metrnl Release', ha='center', fontsize=10)

# Arrow to Systemic Effects
arrow2 = FancyArrow(6, 7.5, 0, -2, width=0.2, color='black')
ax.add_patch(arrow2)

# Draw Systemic Effects
effects_x = [5, 6, 7]
effects_labels = ['Eosinophil Recruitment', 'Tissue Repair', 'Anti-Inflammatory Signaling']
for i, x in enumerate(effects_x):
    effect = Rectangle((x - 0.5, 4.5), 1, 0.5, edgecolor='black', facecolor='lightgreen', lw=2)
    ax.add_patch(effect)
    ax.text(x, 4.75, effects_labels[i], ha='center', fontsize=8)

# Arrows to Tumor Microenvironment
for x in effects_x:
    arrow3 = FancyArrow(x, 4.5, 0, -1, width=0.1, color='black')
    ax.add_patch(arrow3)

# Draw Tumor Microenvironment
tumor = Rectangle((4, 2.5), 2, 1, edgecolor='black', facecolor='lightcoral', lw=2)
ax.add_patch(tumor)
ax.text(5, 3, 'Tumor Microenvironment\n(TME)', ha='center', fontsize=10)

# Arrow to Proposed Interventions
arrow4 = FancyArrow(6, 2.5, 3, -2, width=0.2, color='black')
ax.add_patch(arrow4)

# Draw Proposed Interventions
intervention_labels = ['Personalized\nExercise Protocols', 'Metabolic Support']
intervention_y = [0.5, 0.5]
for i, label in enumerate(intervention_labels):
    rect = Rectangle((7 + i, intervention_y[i]), 1, 1, edgecolor='black', facecolor='lightblue', lw=2)
    ax.add_patch(rect)
    ax.text(7.5 + i, 1, label, ha='center', fontsize=8)

# Save and show
plt.tight_layout()
plt.savefig("graphical_abstract.png", dpi=300)
plt.show()
