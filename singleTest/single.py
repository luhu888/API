#!/usr/bin/env python
# -*- coding: utf_8 -*-
import requests
import xlrd


data = xlrd.open_workbook('D:\JetBrains\PythonProject\APITest\API_source\API.xlsx', 'utf-8')
table = data.sheets()[0]  # 该表的第1个页签
nrows = table.nrows  # 获取表的行数
# print nrows
# for i in range(1, nrows):
# print table.cell_value(0, 0)   # 第1行，第一列
method = table.cell_value(60, 3)
url = table.cell_value(60, 0)
data = table.cell_value(60, 2)
headers = table.cell_value(60, 1)
if data:
    data = eval(data)

if method == 'post':
    if headers == '':
        requests.session().keep_alive = False
        r = requests.post(url=url, json=data)

    else:
        headers = eval(headers)
        requests.session().keep_alive = False
        r = requests.post(url=url, json=data, headers=headers)

elif method == 'get':
    headers = eval(headers)
    r = requests.get(url=url, headers=headers)

elif method == 'put':
    headers = eval(headers)
    r = requests.put(url=url, json=data, headers=headers)

elif method == 'delete':
    headers = eval(headers)
    r = requests.delete(url=url, headers=headers)

print str(url)+'    响应码：' + str(r.status_code)
print r.text
