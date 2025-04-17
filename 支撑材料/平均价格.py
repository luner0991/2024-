"""
    获取平均价格
"""
import pandas as pd

# 读取Excel文件
file_path = '加权单价_2023年统计的相关数据.xlsx'
df = pd.read_excel(file_path)

# 计算销售单价的平均值
def calculate_average_price(price_range):
    low, high = map(float, price_range.split('-'))
    return (low + high) / 2

# 应用函数计算平均值
df['销售单价/(元/斤)'] = df['销售单价/(元/斤)'].apply(calculate_average_price)

# 将修改后的数据保存到新的Excel文件
output_path = '平均价格_2023年统计的相关数据.xlsx'  # 您可以自定义输出文件的名称
df.to_excel(output_path, index=False)  # index=False表示不保存行索引到文件

print("文件已更新，平均价格已计算并保存到新的Excel文件中。")