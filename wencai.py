import pywencai
import os
import datetime

# 获取关键字列表
keywords = os.environ.get("KEYWORD", "").split(',')
now = datetime.datetime.now()
t = now.date()
t2 = t.strftime('%m月%d日')
# 遍历关键字列表进行查询和保存结果
for keyword in keywords:
    filename = f'{keyword}.csv'
    keyword2 = t2+' '+keyword
    res = pywencai.get(query=keyword2, loop=True)
    res.to_csv(filename, index=False, encoding='utf-8-sig')
    print(res)
