import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a new figure
fig, ax = plt.subplots()

# Set limits and aspect
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')

# Define positions for the boxes
positions = {
    "Prior knowledge of state": (1, 8),
    "Prediction step": (5, 8),
    "Measurements": (9, 5),
    "Update step": (5, 5),
    "Next timestep": (5, 2),
    "Output estimate of state": (1, 5)
}

# Draw the boxes
for text, (x, y) in positions.items():
    rect = patches.FancyBboxPatch((x-1, y-0.5), 2, 1, boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightblue")
    ax.add_patch(rect)
    ax.text(x, y, text, ha="center", va="center", fontsize=10)

# Draw the arrows
arrows = [
    ("Prior knowledge of state", "Prediction step"),
    ("Prediction step", "Update step"),
    ("Measurements", "Update step"),
    ("Update step", "Next timestep"),
    ("Next timestep", "Prediction step"),
    ("Update step", "Output estimate of state"),
    ("Output estimate of state", "Prior knowledge of state")
]

for start, end in arrows:
    x1, y1 = positions[start]
    x2, y2 = positions[end]
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", lw=1.5))

# Hide the axes
ax.axis('off')

# Save the figure
plt.savefig("kalman_filter_flow.svg", format="svg")
plt.show()
