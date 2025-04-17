"""
    填充作物类型
"""
import pandas as pd

# 读取两个Excel文件
df1 = pd.read_excel('2023年统计的相关数据.xlsx')  # 假设第一个表格文件名为table1.xlsx
df2 = pd.read_excel('2023年的农作物种植情况.xlsx')  # 假设第二个表格文件名为table2.xlsx

# 合并数据框，基于作物名称和作物编号
merged_df = pd.merge(df1, df2[['作物编号', '作物名称', '作物类型']], on=['作物编号', '作物名称'], how='left')

# 填充作物类型到第一个表格
merged_df['作物类型'] = merged_df['作物类型_x'].combine_first(merged_df['作物类型_y'])

# 删除不需要的辅助列
merged_df.drop(columns=['作物类型_x', '作物类型_y'], inplace=True)

# 保存更新后的表格到新的Excel文件
merged_df.to_excel('作物类型_2023年统计的相关数据.xlsx', index=False)