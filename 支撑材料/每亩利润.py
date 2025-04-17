import pandas as pd

# 读取Excel文件
file_path = '加权单价_2023年统计的相关数据.xlsx'
df = pd.read_excel(file_path)

# 计算每亩利润
df['每亩利润'] = (df['加权单价/(元/斤)'] * df['亩产量/斤']) - df['种植成本/(元/亩)']

# 将结果保存到新的Excel文件
output_path = '每亩利润_2023年统计的相关数据.xlsx'  # 您可以自定义输出文件的名称
df.to_excel(output_path, index=False)  # index=False表示不保存行索引到文件

print(f"计算结果已保存到 {output_path}")