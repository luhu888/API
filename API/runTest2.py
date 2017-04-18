#!/usr/bin/env python
# -*- coding: utf_8 -*-
import unittest
import time
import sys

from templib.HTMLTestRunner import HTMLTestRunner

'''指定目录下的所有测试模块，自动执行所有的测试用例'''

reload(sys)
sys.setdefaultencoding('utf-8')

# 定义测试用例的目录为当前目录
test_dir = './testCase/'
discorver = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H-%M-%S')    # 获取当前的时间，并固定其格式

    filename = './report/' + now + 'test_result.html'    # 定义报告的存放位置
    fp = open(filename, 'wb')   # wb表示有读写权限

    # 定义测试报告
    runner = HTMLTestRunner(stream=fp, title="api测试", description='教学管理系统接口测试报告：')

    # 运行测试

    runner.run(discorver)
    fp.close()      # 关闭文件对象，才能保存数据，生成文档