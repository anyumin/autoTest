#!/user/bin/env python
# -*- coding:utf-8 -*-
# author:yumin An

import pytest
from utils.operationExcel import OperationExcel
from base.method import Requests
from utils.operationMysql import mysqlUtils
import allure
import time

class TestDangdang:
	excel = OperationExcel()
	obj = Requests()
	mysql = mysqlUtils()

	# @pytest.mark.flaky(reruns=5) #失败执行多次
	def test_dangdang_0001(self):
		r = self.obj.request(
			url = self.excel.getUrl(row=1),
			method=self.excel.getMethod(row=1),
			json = self.excel.getDataValue(row=1))
		return r.text
		# assert "您好，欢迎光临乐科二手图书网" in json.dumps(r.text,ensure_ascii=False)
		# assert r.status_code == 200 #断言状态码
	# time.sleep(1)
	# @pytest.mark.repeat(3) #c重复执行
	def test_dangdang_0002(self):
		param = self.excel.getDataValue(row=2)
		r = self.obj.request(
			url = self.excel.getUrl(row=2),
			method=self.excel.getMethod(row=2),
			headers=self.excel.getHeaderss(row=2),
			params=param
		)
		# bookName = self.mysql.readSql(mysql="select * from d_product where id=%s",params=param)
		# assert r.

	# def test_lagou_0003(self):
	# 	r = self.obj.request(
	# 		url = self.excel.getUrl(row=3),
	# 		method=self.excel.getMethod(row=3),
	# 		params = self.excel.getDataValue(row=3))
	# 	print(r.cookies)


if __name__ == '__main__':
	# pytest.main(["-s", "-v", "test_dangdang.py","--alluredir","./report/result"])
	# import subprocess
	# subprocess.call('allure generate report/result/ -o report/html --clean',shell=True)
	# subprocess.call('allure open -h 127.0.0.1 -p  8188 ./report/html',shell=True)

	pytest.main(["-s","-v","-x","test_dangdang.py"])
	# pytest.main(["-s","-v","test_dangdang.py::test_dangdang_0002"])