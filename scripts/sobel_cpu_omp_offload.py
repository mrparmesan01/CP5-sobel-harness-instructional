# import matplotlib.pyplot as plt

# # Define table columns and data rows
# col_labels = ["Implementation", "Runtime (ms)", "Achieved Occupancy (%)", "DRAM Throughput (%)"]
# table_data = [
#     ["OpenMP-Offload (N=1024, B=64)", "1.40", "66.33", "13.77"],
#     ["Native CUDA Best Config", "238.33", "13.11", "0.08"]
# ]

# # Create figure and axis
# fig, ax = plt.subplots(figsize=(9, 2.5), dpi=300)
# ax.axis('off')

# # Create the table
# table = ax.table(
#     cellText=table_data,
#     colLabels=col_labels,
#     loc='center',
#     cellLoc='center'
# )

# # Customize table styling and fonts
# table.auto_set_font_size(False)
# table.set_fontsize(10)
# table.scale(1.2, 1.6)

# # Style header and alternating row colors
# for key, cell in table.get_celld().items():
#     if key[0] == 0:
#         cell.set_facecolor('#2b5c8f')
#         cell.set_text_props(weight='bold', color='white')
#     else:
#         cell.set_facecolor('#f8f9fa' if key[0] % 2 == 1 else '#ffffff')

# plt.title("Performance Comparison: OpenMP-Offload vs. Native CUDA", fontsize=11, fontweight='bold', pad=15)
# plt.tight_layout()

# # Save and display figure
# plt.savefig("sobel_performance_table.png", bbox_inches='tight', dpi=300)
# plt.show()
import matplotlib.pyplot as plt

# Data rows comparing OpenMP-Offload vs. Best CUDA (sobel_gpu at N=512, B=1024)
rows = [
    ["OpenMP-Offload", "1.40 ms", "66.33%", "13.77%"],
    ["CUDA", "238.33 ms", "13.11%", "0.08%"]
]

columns = [
    "Code Version / Configuration", 
    "Runtime", 
    "Achieved Occupancy (%)", 
    "Peak Memory BW (%)"
]

# Set up matplotlib figure
fig, ax = plt.subplots(figsize=(11, 3.2))
ax.axis('off')
ax.axis('tight')

# Create table
table = ax.table(cellText=rows, colLabels=columns, loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(10.5)
table.scale(1.2, 1.8)

# Styling header and cells
for key, cell in table.get_celld().items():
    if key[0] == 0:
        cell.set_facecolor('#2b5b84')
        cell.set_text_props(weight='bold', color='white')
    else:
        cell.set_facecolor('#f4f6f9')

plt.title("OpenMP-Offload vs. CUDA Code", fontsize=13, weight='bold', pad=18)
plt.tight_layout()

# Save figure
plt.savefig("sobel_performance_comparison_table.png", dpi=300)
plt.show()