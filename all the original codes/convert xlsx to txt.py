import pandas as pd
df = pd.read_excel('DETAIL.xlsx', header=None)		# 使用pandas模块读取数据
print('开始写入txt文件...')
df.to_csv('详情页文本.txt', header=None, sep=',', index=False)		# 写入，逗号分隔
print('文件写入成功!')
