# 项目介绍
## testProject  批量测试API接口并自动生成HTML测试报告
	|--API_source  需要请求的接口，以及请求需要传递的参数
		|--GET_API.xlsx
		|--POST_API.xlsx
	|--report     生成的测试报告
		|--xxxx-xx-xx xx-xx-xxtest_result.html
	|--templib     项目中需要使用小模块，比如自动生成身份证号和姓名的模块
		|--HTMLTestRunner.py
		|--number.py
		|--districtcode
	|--testCase    测试用例
		|--test_request_get.py
		|--test_request_get2.py
		|--test_request-post.py
	|--runTest.py    测试用例驱动
	|--rnuTest2.py   自动检测所有测试用例并运行的驱动
