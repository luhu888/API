#!/usr/bin/env python
# -*- coding: utf_8 -*-
import unittest
import requests


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
        data = xlrd.open_workbook('API_source/API.xlsx')
        table = data.sheets()[0]   # 该表的第1个页签
        nrows = table.nrows   # 获取表的行数
        # print nrows
        for i in range(31, 33):
            # print table.cell_value(0, 0)   # 第1行，第一列
            method = table.cell_value(i, 3)
            url = table.cell_value(i, 0)
            data = table.cell_value(i, 2)
            headers = table.cell_value(i, 1)
            self.url = url
            if data:
                self.data = eval(data)

            if method == 'post':
                if headers == '':
                    self.r = requests.post(url=self.url, json=self.data)
                else:
                    self.r = requests.post(url=self.url, json=self.data, headers=eval(headers))
            elif method == 'get':
                self.r = requests.get(url=self.url, headers=eval(headers))
            elif method == 'put':
                self.r = requests.put(url=self.url, json=self.data, headers=eval(headers))
            elif method == 'delete':
                self.r = requests.delete(url=self.url, headers=eval(headers))

            print url+'     响应码:' + str(self.r.status_code)+''
            print self.r.text
            print '#####################################################################################'

