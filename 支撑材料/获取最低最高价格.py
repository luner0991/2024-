"""
    用于获得最低和最高价格
"""
import pandas as pd

# 读取Excel文件
df = pd.read_excel('作物类型_2023年统计的相关数据.xlsx')  # 替换 'your_file.xlsx' 为你的文件名

# 定义一个函数来处理价格区间
def split_price(price_range):
    # 分割价格区间并返回最低和最高价格
    prices = price_range.split('-')
    return float(prices[0]), float(prices[1])

# 应用函数并创建新的列
df[['最低价格', '最高价格']] = df.apply(lambda row: split_price(row['销售单价/(元/斤)']), axis=1, result_type='expand')

# 保存更新后的表格到新的Excel文件
df.to_excel('最低最高单价_2023年统计的相关数据.xlsx', index=False)  # 你可以选择一个新的文件名来保存
