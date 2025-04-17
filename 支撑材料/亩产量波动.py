import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import numpy as np

# 读取数据
df = pd.read_csv('最终价格_2024_2025.csv')

# 初始化一个空的DataFrame来存储预测结果，确保列名与原始数据一致（这里假设有作物名称、地块类型和2023-2030年的价格列）
predictions = pd.DataFrame(columns=['作物名称', '地块类型'] + [f'{year}价格' for year in range(2023, 2031)])

# 对每种作物和地块类型进行分组，并预测价格
grouped = df.groupby(['作物名称', '地块类型'])
for (crop, land_type), group in grouped:
    historical_prices = group[['2023价格', '2024价格', '2025价格']].values.flatten()  # 将价格数据展平为一维数组

    # 检查数据是否包含NaN值
    if np.isnan(historical_prices).any():
        continue  # 跳过包含NaN的数据组

    # 尝试使用ARIMA模型进行预测（这里使用简单的ARIMA(1,0,1)作为示例）
    try:
        model = ARIMA(historical_prices, order=(1, 0, 1))
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=5)  # 预测未来的5个价格点

        # 创建新的行来存储预测结果
        new_row = [crop, land_type] + [np.nan] * 3  # 2023-2025年的价格已经是历史数据，所以这里填NaN（或者可以是实际值）
        new_row += list(forecast)  # 添加预测的价格
        new_row += [np.nan] * (2030 - 2025 - 1 - len(forecast))  # 填充剩余年份的NaN（如果有的话）

        # 使用loc来添加新行到predictions DataFrame中
        predictions.loc[len(predictions)] = new_row
    except Exception as e:
        print(f"Error predicting for {crop} on {land_type}: {e}")

    # 保存预测结果到新的CSV文件
predictions.to_csv('crop_prices_predictions.csv', index=False)
print("预测结果已保存到 'crop_prices_predictions.csv'")