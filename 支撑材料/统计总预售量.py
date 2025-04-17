import pandas as pd

# 读取Excel文件
df = pd.read_excel('2023年农作物各类数据最终版1.1.xlsx')  # 替换 'your_file.xlsx' 为你的文件名

# 打印原始数据（可选）
print("原始数据:")
print(df)

# 统计每种作物名称的总预售量（亩）
total预售量 = df.groupby('作物名称')['预售量（亩）'].sum()

# 打印统计结果
print("每种作物名称的总预售量（亩）:")
print(total预售量)

# 将结果保存到新的Excel文件
total预售量.to_excel('总预售量_2023年农作物各类数据最终版1.1.xlsx')  # 保存到新的文件