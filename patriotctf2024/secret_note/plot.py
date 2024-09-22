import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import matplotlib.patches as mpatches

# Replace 'your_file.csv' with the path to your CSV file
df = pd.read_csv('data.csv')

# Define colors based on button states
color_dict = {
    (False, False): 'blue',    # No buttons held
    (True, False): 'green',    # Left button held
    (False, True): 'red',      # Right button held
    (True, True): 'purple'     # Both buttons held
}

label_dict = {
    (False, False): 'No buttons held',
    (True, False): 'Left button held',
    (False, True): 'Right button held',
    (True, True): 'Both buttons held'
}

# Create a color column based on button states
df['color'] = df.apply(
    lambda row: color_dict[(row['left_button_holding'], row['right_button_holding'])],
    axis=1
)

# Prepare data for LineCollection
points = df[['x', 'y']].values
segments = [points[i:i+2] for i in range(len(points)-1)]
segment_colors = df['color'].values[:-1]

# Create LineCollection
lc = LineCollection(segments, colors=segment_colors, linewidths=2)

# Plotting
fig, ax = plt.subplots()
ax.add_collection(lc)
ax.autoscale()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Mouse Movement Trajectory')

# Create legend
patches = [mpatches.Patch(color=color_dict[key], label=label_dict[key]) for key in color_dict]
plt.legend(handles=patches, title='Button States')

plt.show()
