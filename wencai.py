import pywencai
import os
import datetime

# 获取关键字列表
keywords = os.environ.get("KEYWORD", "").split(',')
today = datetime.day.today()
tomorrow = today + datetime.timedelta(days=1)
t2 = tomorrow.strftime('%m月%d日')
# 遍历关键字列表进行查询和保存结果
for keyword in keywords:
    filename = f'{keyword}-{tomorrow}.csv'
    keyword2 = t2+' '+keyword
    res = pywencai.get(query=keyword2, loop=True)
    res.to_csv(filename, index=False, encoding='utf-8-sig')
    print(res)
