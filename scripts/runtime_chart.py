import matplotlib.pyplot as plt
import numpy as np

# Set seaborn/matplotlib style for a clean, publication-ready look
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10

# Data for concurrency levels and runtimes
concurrency_levels = [1, 2, 4, 8, 16]
runtimes_ms = [337.80, 214.39, 112.47, 81.09, 57.75]

# Create a smaller figure and axis (e.g., 6x3.5 inches)
fig, ax = plt.subplots(figsize=(6, 3.5), dpi=300)

# Plot the runtime line with markers
ax.plot(concurrency_levels, runtimes_ms, marker='o', color='#1f77b4', linewidth=2, 
        markersize=6, label='sobel_cpu (OpenMP)')

# Annotate each data point with its exact runtime value
for x, y in zip(concurrency_levels, runtimes_ms):
    ax.annotate(f'{y:.2f} ms', 
                xy=(x, y), 
                xytext=(0, 8),  # 8 points vertical offset
                textcoords='offset points', 
                ha='center', 
                fontsize=9, 
                fontweight='semibold',
                color='#333333')

# Set chart title and axis labels with smaller font sizes
ax.set_title('CPU OpenMP Parallel Runtime vs. Concurrency Level', fontsize=11, fontweight='bold', pad=12)
ax.set_xlabel('Concurrency Level (Number of Threads)', fontsize=10, labelpad=8)
ax.set_ylabel('Elapsed Runtime (ms)', fontsize=10, labelpad=8)

# Configure ticks
ax.set_xticks(concurrency_levels)
ax.set_xticklabels([str(c) for c in concurrency_levels])

# Set axis limits with nice padding
ax.set_xlim(0.5, 17.5)
ax.set_ylim(0, 390)

# Add legend and tight layout
ax.legend(frameon=True, facecolor='white', edgecolor='none', loc='upper right', fontsize=9)
plt.tight_layout()

# Save the figure to disk and display it
plt.savefig('sobel_cpu_runtime_scaling_small.png', dpi=300)
plt.show()