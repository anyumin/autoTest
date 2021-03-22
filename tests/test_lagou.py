#!/user/bin/env python
# -*- coding:utf-8 -*-
# author:yumin An

from utils.operationExcel import OperationExcel
from base.method import Requests
import pytest


#读取文件
class Testlagou:
	excel = OperationExcel()
	req = Requests()


	def test_listLaGou(self,first=True,pn=None,kd=None):
		data = self.excel.getDataValue(row=4)
		header = self.excel.getHeaderss(row = 4)
		data['first'] = first
		data['pn'] = pn
		data['kd'] = kd
		r = self.req.request(
			url = self.excel.getUrl(row = 4),
			method=self.excel.getMethod(row = 4),
			headers = self.excel.getHeaderss(row=4),
			params = data
		)
		return r
		# print(header)

	def test_list_0001(self):
		'''测试kd为空'''
		response = self.test_listLaGou(pn=2)
		# assert response.json() != {}
	def test_list_0002(self):
		'''测试超过页数查询'''
		response = self.test_listLaGou(pn=65)
		# assert response.json() == {}
		print(response.json())


if __name__ == '__main__':
	pytest.main(["-s","-v","test_lagou.py"])