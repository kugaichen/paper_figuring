'''
A python file for obtainning the approiate bar chart/histogram figure for paper writing or data illustration
author: kugaichen
'''
import os
import numpy as np 
import matplotlib.pyplot  as plt 
 

# ---------- x_axis/y_axis categories/data/labels configuration --------
# categories Definition (the distinct category of X_axis)
categories = ['dataset1', 'dataset2', 'dataset3', 'dataset4', 'dataset5', 'dataset6', 'dataset7', 'dataset8', 'dataset9']

# the data of every distinct category of X_axis 
# # Evaluation1: data 
Evaluation1_method1 = np.array([4096, 8192, 16384, 2048, 6144, 32768, 10240, 65536, 131072]) / 1024       # 4, 8, 16, 2, 6, 32, 10, 64, 128 GB
Evaluation1_method2 = np.array([2048, 4096, 8192, 1024, 3072, 16384, 5120, 32768, 65536]) / 1024          # 2, 4, 8, 1, 3, 16, 5, 32, 64 GB  
Evaluation1_method3 = np.array([1024, 2048, 4096, 512, 1536, 8192, 2560, 16384, 32768]) / 1024            # 1, 2, 4, 0.5, 1.5, 8, 2.5, 16, 32 GB
Evaluation1_method4 = np.array([512, 1024, 2048, 256, 768, 4096, 1280, 8192, 16384]) / 1024               # 0.5, 1, 2, 0.25, 0.75, 4, 1.25, 8, 16 GB
Evaluation1_method5 = np.array([256, 512, 1024, 128, 384, 2048, 640, 4096, 8192]) / 1024                  # 0.25, 0.5, 1, 0.125, 0.375, 2, 0.625, 4, 8 GB

# # Evaluation2: data 
# Evaluation2_method1 = np.array([45000, 89000, 185000, 23000, 76000, 156000, 67000, 198000, 445000]) / 1000
# Evaluation2_method2 = np.array([12000, 18000, 48000, 6500, 24000, 52000, 15000, 68000, 128000]) / 1000
# Evaluation2_method3 = np.array([3200, 5800, 14500, 1800, 7200, 18500, 4200, 22000, 58000]) / 1000
# Evaluation2_method4 = np.array([980, 1650, 4200, 520, 2100, 6800, 1200, 8500, 18500]) / 1000
# Evaluation2_method5 = np.array([280, 520, 1350, 165, 680, 2200, 380, 2800, 6500]) / 1000

# Consolidate data for plotting
# Note: The variable names values1, values2, etc. are kept to minimize changes in the plotting section.
values1 = Evaluation1_method1      
values2 = Evaluation1_method2    
values3 = Evaluation1_method3
values4 = Evaluation1_method4
values5 = Evaluation1_method5 


# --------------- Plotting Configuration -----------------

# Define colors for the bars
colors = [
    "#4E79A7",  # Blue
    "#F28E2B",  # Orange
    "#E15759",  # Red
    "#76B7B2",  # Teal
    "#59A14F",  # Green
    "#EDC949"   # Yellow
]
 
# Bar labels and corresponding hatch patterns
bar_labels = ['method1', 'method2', 'method3', 'method4', 'method5']
bar_hatches = ["ooo", "\\\\", "...", "OOO", "///"]
plt.rcParams['hatch.linewidth'] = 0.7 


# Corresponding data series and colors (ensure order matches bar_labels)
data_series = [values1, values2, values3, values4, values5]
bar_colors = [colors[0], colors[4], colors[1], colors[3], colors[2]] # Custom color assignment 
 
# --- Initialize Figure and Axes ---

fig, ax = plt.subplots(figsize=(7, 4), dpi=300)   # The higher the DPI, the clearer the image (but the file size will also increase)

# --- Plotting the Bars ---
# Loop through the data series to create bars
num_series = len(data_series)
x = np.arange(len(categories)) * 5  # Multiplier for spacing between category groups (调整柱子的间距)
width = 0.7  # Width of individual bars (调整柱子的宽度)

for i, (data, label, color, hatch_pattern) in enumerate(zip(data_series, bar_labels, bar_colors, bar_hatches)):
    # Calculate offset for each bar in a group
    # The offset centers the group of bars around the x-tick
    offset = (i - num_series / 2 + 0.5) * width
    ax.bar(x + offset, data, width, label=label, color=color, 
           hatch=hatch_pattern, edgecolor='black', linewidth=0.7, alpha=0.8)


# --- x axis setting ---
ax.set_xlabel('Rule  Set', fontsize = 14)  # 设置X轴标题
ax.set_xticks(x) # 设置X轴刻度位置为x数组的值
ax.set_xticklabels(categories,  fontsize= 12) # 设置X轴刻度标签为categories，字体大小20
plt.xticks(rotation=30)  # 将X轴标签旋转30度

# 定义 x轴下的不同类别规则集的区分线（用虚线分割不同的ruleset）
grid_positions = [12.5, 27.5]  # 定义垂直分隔线位置
ax.set_xticks(grid_positions, minor=True)  # 在指定位置设置次要刻度

# 隐藏主要刻度的网格线
ax.grid(axis='x', which='major', alpha=0.0)  # 完全隐藏主网格线

# 显示次要刻度的网格线（用作分组分隔线）
ax.grid(axis='x', which='minor', linestyle='--', linewidth=1.5, alpha=0.8)
ax.xaxis.set_tick_params(which='minor', length=0)  # 隐藏次要刻度标记，只保留网格线



# --- y axis setting ---
ax.set_ylabel('Evaluation Criteria', fontsize = 14) # 设置Y轴标题
ax.tick_params(axis='y', labelsize=12) # 设置y轴刻度字体大小
ax.set_yscale('log', base = 2) # 将Y轴设置为以2为底的对数刻度

min_value = min([min(values) for values in [values1, values2, values3, values4, values5] if len(values) > 0])
ax.set_ylim(min_value * 0.8, max(values1) * 1.2)  # 设置Y轴范围，上限为最大值的1.2倍
ax.yaxis.grid(True, linestyle='--', linewidth=1, alpha=0.7)  # 添加Y轴网格线（虚线样式）



# --- plot setting ---
ax.set_axisbelow(True)  # 将网格线置于图表元素下方

# 设置图例位置和样式
ax.legend(loc='upper left', ncol=2, fontsize=12, frameon=True, 
          edgecolor='gray', bbox_to_anchor=(0, 1.0),
          columnspacing=0.6, handletextpad=0.4)  # 紧凑的图例布局

plt.tight_layout(pad=1.0)  # 减小边距
ax.margins(x=0.03, y=0.03)  # 设置图表边距

# 保存图片
output_dir = r".\result"
output_path = r".\result\output.png"

# 创建文件夹（如果不存在）
os.makedirs(output_dir, exist_ok=True)

# 保存图片
plt.savefig(output_path, bbox_inches='tight', dpi=300, facecolor='white')
print(f"图片已保存到: {output_path}")

plt.show()  # 显示图表

