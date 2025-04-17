import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['KaiTi']
plt.rcParams['axes.unicode_minus']=False
import numpy as np

# 读取Excel文件
file_path = '亩产量预测.xlsx'  # 请根据实际文件路径修改
df = pd.read_excel(file_path, index_col='Crop')

# 转置DataFrame，使作物成为行，年份成为列
df = df.T

# 计算相关系数矩阵
correlation_matrix = df.corr()

# 找出负相关性最大的农作物对，且相关性小于-0.97
# 先将矩阵flatten为一个序列，然后找出满足条件的值
flat_corr = correlation_matrix.unstack()
negative_corr_pairs = flat_corr[(flat_corr < -0.97)].dropna()

# 按相关性强度（绝对值）排序
negative_corr_pairs = negative_corr_pairs.sort_values(ascending=True, key=abs)

# 选择负相关性最大的5对农作物
top_5_negative_pairs = negative_corr_pairs.head(5)

# 打印负相关性最大的5对农作物
print("负相关性最大的5对农作物:")
for index, value in top_5_negative_pairs.items():
    print(f"{index[0]} 和 {index[1]} 的相关性为 {value:.4f}")

# 绘制热力图
selected_crops = np.unique(top_5_negative_pairs.index.get_level_values(0))
selected_crops = np.append(selected_crops, top_5_negative_pairs.index.get_level_values(1))
selected_crops = np.unique(selected_crops)
selected_crops = list(selected_crops)  # 转换为列表

plt.figure(figsize=(10, 8))
ax = sns.heatmap(correlation_matrix.loc[selected_crops, selected_crops], annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Top 5 Negative Correlation Crops Heatmap')
# 设置x轴和y轴的标签
plt.xticks(range(len(selected_crops)), selected_crops, rotation=90)
plt.yticks(range(len(selected_crops)), selected_crops)
plt.show()