import pywencai
import os
import datetime
import pandas as res
import openpyxl

# 获取关键字列表
keywords = os.environ.get("KEYWORD", "").split(',')
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
t2 = tomorrow.strftime('%m月%d日')

# 遍历关键字列表进行查询和保存结果
for keyword in keywords:
    filename = f'{keyword}-{tomorrow}.csv'
    keyword2 = t2+' '+keyword
    res = pywencai.get(query=keyword2, loop=True)
    columns_to_select = [0, 1, 5, 10]
    # 使用iloc来截取列
    selected_res = res.iloc[:, columns_to_select]
    if res is None:
        raise ValueError("Did not receive any data. The result is None.")
    selected_res.to_csv(filename, index=False, encoding='utf-8-sig')
    selected_res.to_excel('{filename}.xlsx', index=False)  # index=False表示不写入行索引 
    #print(selected_res)
