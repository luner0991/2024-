import pandas as pd
import numpy as np


# 读取Excel文件
def read_excel(file_path):
    return pd.read_excel(file_path, index_col=0)


# 写入Excel文件
def write_excel(dataframe, file_path):
    dataframe.to_excel(file_path, index=True)


# 生成2024年的数据
def generate_2024_data(historic_data):
    n_rows, n_cols = historic_data.shape
    new_year_data = historic_data.copy()

    # 遍历每个地块
    for row_index in range(1, n_rows + 1):
        current_crops = historic_data.iloc[row_index - 1, 1:].values
        new_crops = [0] * (n_cols - 1)  # 初始化新作物数组

        # 尝试为当前地块找到一个新的作物组合
        for col_index in range(n_cols - 1):
            if current_crops[col_index] > 0:
                # 避免在同一地块上种植相同的作物
                possible_crops = [crop for crop in range(1, n_cols + 1) if crop != current_crops[col_index]]
                new_crops[col_index] = possible_crops[np.random.choice(len(possible_crops))]  # 随机选择一个不同的作物

        # 更新数据
        new_year_data.iloc[row_index - 1, 1:] = new_crops

    return new_year_data

# 主函数
def main():
    file_path = '2023年ABC地块数据.xlsx'
    data_2023 = read_excel(file_path)
    data_2024 = generate_2024_data(data_2023)
    output_file_path = '2024年ABC地块数据.xlsx'
    write_excel(data_2024, output_file_path)


if __name__ == "__main__":
    main()