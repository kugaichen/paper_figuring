import numpy as np 
import matplotlib.pyplot as plt 
import os

# --- Global Plot Settings ---
plt.rcParams.update({'font.size': 20})
# plt.rcParams['hatch.linewidth'] = 0.4  # 设置hatch线条宽度

# --- Data Definition ---
categories = ['dataset1', 'dataset2', 'dataset3', 'dataset4', 'dataset5', 'dataset6', 'dataset7', 'dataset8', 'dataset9']

# Phase2 Memory EqIDTable (KB to MB conversion)
Evaluation_method1 = np.array([2024, 4096, 4192, 1512, 2048, 3144, 5024, 10192, 12384]) / 1024       # RFC: 1, 4, 8, 0.5, 2, 6, 1, 8, 16 MB
Evaluation_method2 = np.array([1512, 3048, 3096, 1056, 1524, 2472, 4012, 8096, 9192]) / 1024 
# Calculate reduction percentage
reduction_percentage = (Evaluation_method1 - Evaluation_method2) / Evaluation_method1 * 100

# --- Plotting Configuration ---
x = np.arange(len(categories)) * 1.0  # X-axis positioning
width = 0.3  # Bar width

# Define colors
colors = [
    "#4E79A7",  # Blue
    "#F28E2B",  # Orange
    "#E15759",  # Red
    "#76B7B2",  # Teal
    "#59A14F",  # Green
    "#EDC949"   # Yellow
]

# --- Initialize Figure and Axes ---
fig, ax = plt.subplots(figsize=(7, 4), dpi=300)  

# --- Plotting the Bars ---
ax.bar(x - 0.5 * width, Evaluation_method1, width, label='method1', color=colors[0], 
       hatch="oo", edgecolor='black', linewidth=0.4, alpha=0.85)
ax.bar(x + 0.5 * width, Evaluation_method2, width, label='method2', color=colors[2], 
       hatch="///", edgecolor='black', linewidth=0.4, alpha=0.85)

# --- X-axis Configuration ---
ax.set_xlabel('Rule  Set', fontsize = 14)  # 设置X轴标题
ax.set_xticks(x) # 设置X轴刻度位置为x数组的值
ax.set_xticklabels(categories,  fontsize= 12) # 设置X轴刻度标签为categories，字体大小20
plt.xticks(rotation=30)  # 将X轴标签旋转30度

# 定义 x轴下的不同类别规则集的区分线（用虚线分割不同的ruleset）
grid_positions = [2.5, 5.5] # 定义垂直分隔线位置
ax.set_xticks(grid_positions, minor=True)  # 在指定位置设置次要刻度

# 隐藏主要刻度的网格线
ax.grid(axis='x', which='major', alpha=0.0)  # 完全隐藏主网格线

# 显示次要刻度的网格线（用作分组分隔线）
ax.grid(axis='x', which='minor', linestyle='--', linewidth=1.5, alpha=0.8)
ax.xaxis.set_tick_params(which='minor', length=0)  # 隐藏次要刻度标记，只保留网格线


# --- Y-axis Configuration ---
ax.set_ylabel('Evaluation Criteria', fontsize = 14) # 设置Y轴标题
ax.tick_params(axis='y', labelsize=12) # 设置y轴刻度字体大小
ax.set_yscale('log', base = 2) # 将Y轴设置为以2为底的对数刻度

min_value = min([min(values) for values in [Evaluation_method1,Evaluation_method2] if len(values) > 0])
max_value = max([max(values) for values in [Evaluation_method1,Evaluation_method2] if len(values) > 0])
ax.set_ylim(min_value * 0.8, max_value * 8)  # 设置Y轴范围，上限为最大值的1.2倍
ax.yaxis.grid(True, linestyle='--', linewidth=1, alpha=0.7)  # 添加Y轴网格线（虚线样式）

# 创建第二个 y 轴
ax2 = ax.twinx()

# 绘制折线图（减少的百分比）
ax2.plot(x, reduction_percentage, color=colors[1], marker='.', linestyle='-', linewidth= 0.7, label='Reduction Percentage')

# 设置第二个 y 轴的标签
ax2.set_ylabel('Reduction Percentage (%)',fontsize = 14)
ax2.tick_params(axis='y',labelsize = 12)

# 设置第二个 y 轴的范围
ax2.set_ylim(0, max(reduction_percentage) * 1.15)



# --- plot setting ---
ax.set_axisbelow(True)  # 将网格线置于图表元素下方

# 设置图例位置和样式
ax.legend(loc='upper left', ncol=1, fontsize=10, frameon=True, 
          edgecolor='gray', bbox_to_anchor=(0, 1.0),
          columnspacing=0.6, handletextpad=0.4)  # 紧凑的图例布局

# 设置第二个Y轴的图例（折线图）
ax2.legend(loc='upper right', fontsize=10, frameon=True, 
           edgecolor='gray', bbox_to_anchor=(1.0, 1.0))

plt.tight_layout(pad=1.0)  # 减小边距
ax.margins(x=0.03, y=0.03)  # 设置图表边距

# 保存图片
output_dir = r".\result"
output_path = r".\result\histogram_with_line.png"

# 创建文件夹（如果不存在）
os.makedirs(output_dir, exist_ok=True)

# 保存图片
plt.savefig(output_path, bbox_inches='tight', dpi=300, facecolor='white')
print(f"图片已保存到: {output_path}")

plt.show()  # 显示图表
