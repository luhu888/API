# __author__=luhu
# -*- coding: utf-8 -*-
import json
import jsonschema
import requests

url = 'http://test2.xinheyun.com/api/v2/products?filters=%5B%5D&length=10&search_map=%5B%5D&start=0&type=products'
cookie = {'_ga': 'GA1.2.580916110.1530770314', '_gid': 'GA1.2.1580582036.1530770314', '__lnkrntdmcvrd': '-1', 'AUTHOR': 'ZORIGT', 'STAFF_ID': '3893', 'TENANT_ID': 'dceb93ab-3f89-45e5-9aad-1953b484816d', 'SESSION': 'c666b719-44a0-43f6-b9d7-3518a7cb2af8', '_gat': '1', 'TOKEN': '095370DAF1B3AEC8513C177F3C035580'}
r = requests.post(url=url, cookies=cookie)
print(r.status_code)
data = json.loads(r.text)
response = json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)
print(response)
schema = {"type": "object", "properties": {"price": {"type": "number"}, "name": {"type": "string"}, }}
jsonschema.validate(response, schema)
print('校验通过！！！')
