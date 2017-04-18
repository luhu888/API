# __author__=luhu
# -*- coding: utf-8 -*-
import requests
import xlrd


data = xlrd.open_workbook('D:\JetBrains\PythonProject\API\API_source\API.xlsx')
table = data.sheets()[0]  # 该表的第1个页签
nrows = table.nrows  # 获取表的行数
# print nrows
for i in range(1, nrows):
    # print table.cell_value(0, 0)   # 第1行，第一列
    method = table.cell_value(i, 3)
    url = table.cell_value(i, 0)
    data = table.cell_value(i, 2)
    headers = table.cell_value(i, 1)
    if data:
        data = eval(data)
    headers = eval(headers)
    if method == 'post':
        if not headers:
            r = requests.post(url=url, json=data)
        else:
            r = requests.post(url=url, json=data, headers=headers)
    elif method == 'get':
        r = requests.get(url=url, headers=headers)
    elif method == 'put':
        r = requests.put(url=url, json=data, headers=headers)
    elif method == 'delete':
        r = requests.delete(url=url, headers=headers)

    print url
    print '响应码：：：' + str(r.status_code)
    print r.text
