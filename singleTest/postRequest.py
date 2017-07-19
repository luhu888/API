# __author__=luhu
# -*- coding: utf-8 -*-
import requests

url = 'http://192.168.1.102:9999/pre_student/bulk_create/'
headers = {"Authorization": "Token b0a872460239b0fd8dab1b6c93718a7f39a9536a"}
# json = {"ids": [1, 3, 5], "data": "{'follower': 2, 'source': 2, 'intent_grade': 1, 'category': 1, 'next_follow_time': '2017-06-22T12:12'}"}
json2 = [{'user': {'name': '1ykh', 'tel': '15856121999'}, 'follower': 'root', 'courses': '语文课', 'source': '准学员来源1',
          'category': '准学员所属分类1', 'intent_grade': '不想去', 'remark': '批量添加的', 'tags': '标记',
          'next_follow_time': '2017-05-12 00:00:00'}, ]
r = requests.post(url=url, headers=headers, json=json2)
print r.status_code
print r.text
