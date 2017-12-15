#!/usr/bin/env python
# -*- coding: utf_8 -*-
import unittest
from time import sleep

import requests
import ast
import xlrd


class MyTest(unittest.TestCase):  # 封装测试环境的初始化和还原的类
    def setUp(self):
        print 'start test'
        pass

    def tearDown(self):
        print 'end test'
        pass


class test_userAPI(MyTest):    # 将单个接口封装成一个类，其中的方法是具体的测试用例

    def test_userAPI(self):     # self.用在方法属性中，表示该方法的属性，不会影响其他方法的属性
        data = xlrd.open_workbook('D:\JetBrains\PythonProject\APITest\API_source\API.xlsx')
        table = data.sheets()[0]   # 该表的第1个页签
        nrows = table.nrows   # 获取表的行数
        # print nrows
        for i in range(2, nrows):
            # print table.cell_value(0, 0)   # 第1行，第一列
            method = table.cell_value(i, 3)
            url = table.cell_value(i, 0)
            data = table.cell_value(i, 2)
            headers = table.cell_value(i, 1)
            self.url = url
            # s = ast.literal_eval(data).values()
            if data:
                self.data = ast.literal_eval(data)
                # print self.data
            if method == 'post':
                if headers == '':
                    self.r = requests.post(url=self.url, json=self.data)
                # if isinstance(s, list):
                #     date = ast.literal_eval(data)
                #     disc = date.get('discount_coupon_record')
                #     its = date.get('items')
                #     event = date.get('event')
                #     student = date.get('student')
                #
                #     self.data = {'discount_coupon_record': disc, 'items': [json.dumps(its)],
                #                  'event': event, 'student': student}
                #     print self.data
                #     # print type(json.dumps(its))
                #     self.r = requests.post(url=self.url, json=self.data, headers=ast.literal_eval(headers))
                else:
                    self.r = requests.post(url=self.url, json=self.data, headers=ast.literal_eval(headers))
            elif method == 'get':
                self.r = requests.get(url=self.url, headers=ast.literal_eval(headers))
            elif method == 'put':
                self.r = requests.put(url=self.url, json=self.data, headers=ast.literal_eval(headers))
            elif method == 'delete':
                self.r = requests.delete(url=self.url, headers=eval(headers))
            elif method == 'patch':
                self.r = requests.patch(url=self.url, json=self.data, headers=ast.literal_eval(headers))

            print url+'     响应码:'.decode('utf-8') + str(self.r.status_code)+''
            print self.r.content
            print '#####################################################################################'
            sleep(0.1)
            print '睡一毫秒'

