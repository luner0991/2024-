import pandas as pd

# 读取Excel文件
df = pd.read_excel('wgx_23年农作物价格表.xlsx')  # 替换 'your_file.xlsx' 为你的文件名

# 定义一个函数来计算加权单价
def calculate_weighted_price(row):
    if row['作物类型'] == '粮食' or row['作物类型'] == '粮食（豆类）':
        return 4 * (row['最低单价'] + row['平均单价']) + 8 * (row['平均单价'] + row['最高单价'])
    elif row['作物类型'] == '蔬菜' or row['作物类型'] == '蔬菜（豆类）':
        return 10 * (row['最低单价'] + row['平均单价']) + 2 * (row['平均单价'] + row['最高单价'])
    elif row['作物类型'] == '食用菌':
        return 7 * (row['最低单价'] + row['平均单价']) + 5 * (row['平均单价'] + row['最高单价'])
    else:
        return None  # 如果作物类型不匹配，返回None

# 应用函数计算加权单价
df['加权单价/(元/斤)'] = df.apply(calculate_weighted_price, axis=1)

df['加权单价/(元/斤)'] = df['加权单价/(元/斤)']*1.0/24
# 保存更新后的表格到新的Excel文件
df.to_excel('wgx_加权单价_2023年统计的相关数据.xlsx', index=False)  # 你可以选择一个新的文件名来保存