# 导入pandas库，用于数据处理和分析

import pandas as pd

# 定义一个字典，包含三列数据：Name, Age, City
# 这里的数据是为了示例如何创建一个DataFrame
data = {
    'Name': ['John', 'Jane', 'Jim'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# 将字典数据转换为DataFrame
# DataFrame是pandas库中的一种数据结构，用于存储表格数据
df = pd.DataFrame(data)