import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots()

# Define a skin-tone color (can adjust this as needed)
skin_color = '#f5cba7'  # light beige/skin tone
nipple_color = '#d98880'  # reddish for nipples

# Left circle (breast)
left_circle = patches.Circle((-1, 0), 1, edgecolor='black', facecolor=skin_color, linewidth=2)
ax.add_patch(left_circle)

# Right circle (breast)
right_circle = patches.Circle((1, 0), 1, edgecolor='black', facecolor=skin_color, linewidth=2)
ax.add_patch(right_circle)

# Nipples (smaller circles)
left_nipple = patches.Circle((-1, 0), 0.1, edgecolor=nipple_color, facecolor=nipple_color)
right_nipple = patches.Circle((1, 0), 0.1, edgecolor=nipple_color, facecolor=nipple_color)
ax.add_patch(left_nipple)
ax.add_patch(right_nipple)

# Set display parameters
ax.set_aspect('equal')
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-1.5, 1.5)
ax.axis('off')
plt.show()