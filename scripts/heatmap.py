import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set style for publication-quality figures
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 8

# Define axes parameters
block_sizes = [32, 64, 128, 256, 512, 1024]
num_blocks = [1, 4, 16, 64, 256, 1024, 4096]

# 1. Runtime Matrix (ms) - Rows: Block Sizes, Columns: Number of Blocks
runtime_matrix = np.array([
    [240.32, 241.77, 243.26, 245.82, 242.36, 252.56, 245.45], # N=32
    [244.65, 240.68, 246.61, 241.75, 239.36, 246.89, 243.52], # N=64
    [251.59, 254.01, 239.29, 242.74, 257.23, 242.12, 242.45], # N=128
    [244.93, 255.23, 245.23, 246.14, 252.11, 241.84, 239.25], # N=256
    [253.52, 241.69, 246.26, 240.76, 258.49, 238.33, 247.35], # N=512
    [256.24, 240.23, 246.61, 239.78, 245.63, 252.32, 243.74]  # N=1024
])

# 2. Achieved Occupancy Matrix (%)
occupancy_matrix = np.array([
    [12.60, 12.42, 13.24, 13.05, 12.53, 12.21, 12.56], # N=32
    [12.81, 12.70, 12.45, 12.51, 12.54, 12.20, 12.57], # N=64
    [12.06, 12.00, 12.54, 12.41, 12.53, 12.45, 13.02], # N=128
    [12.92, 11.89, 12.33, 12.23, 11.87, 12.55, 12.61], # N=256
    [11.94, 12.53, 12.47, 12.52, 11.42, 13.11, 12.99], # N=512
    [11.76, 12.96, 12.47, 12.84, 12.96, 12.11, 12.83]  # N=1024
])

# 3. Peak Memory Bandwidth Throughput Matrix (%)
dram_throughput_matrix = np.array([
    [0.08, 0.08, 0.07, 0.07, 0.08, 0.07, 0.07], # N=32
    [0.07, 0.08, 0.07, 0.08, 0.08, 0.07, 0.07], # N=64
    [0.07, 0.07, 0.08, 0.07, 0.07, 0.08, 0.07], # N=128
    [0.07, 0.07, 0.07, 0.07, 0.07, 0.08, 0.08], # N=256
    [0.07, 0.08, 0.07, 0.08, 0.07, 0.08, 0.07], # N=512
    [0.07, 0.08, 0.07, 0.08, 0.07, 0.07, 0.07]  # N=1024
])

# Create a much smaller figure size (11x3.2 inches)
fig, axes = plt.subplots(1, 3, figsize=(11, 3.2), dpi=300)

metrics = [
    ("Runtime Duration (ms)", runtime_matrix, "Blues", ".1f"),
    ("Achieved Occupancy (%)", occupancy_matrix, "Greens", ".1f"),
    ("Peak Memory Bandwidth (%)", dram_throughput_matrix, "Oranges", ".2f")
]

for ax, (title, data, cmap, fmt) in zip(axes, metrics):
    sns.heatmap(data, annot=True, fmt=fmt, cmap=cmap, cbar=True,
                xticklabels=num_blocks, yticklabels=block_sizes, ax=ax, linewidths=.4,
                annot_kws={"size": 6.5})
    ax.set_title(title, fontsize=9, fontweight='bold', pad=6)
    ax.set_xlabel("Number of Thread Blocks (B)", fontsize=8, labelpad=4)
    ax.set_ylabel("Threads per Thread Block (N)", fontsize=8, labelpad=4)
    ax.tick_params(axis='both', labelsize=7)

plt.suptitle("CUDA Sobel Kernel Performance Metrics Across Launch Configurations", fontsize=10, fontweight='bold', y=1.03)
plt.tight_layout()

# Save figure
plt.savefig("sobel_gpu_heatmaps_compact.png", dpi=300, bbox_inches='tight')
plt.show()