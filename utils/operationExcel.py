#!/user/bin/env python
# -*- coding:utf-8 -*-
# author:yumin An

import xlrd
import json
from common.public import filePath
from utils.operationYaml import OperationYaml
import utils.readConfig

class ExcelVarles:
	caseID=0
	des=1
	url=2
	method=3
	headerss=4
	data=5
	expect=6

	@property
	def getCaseID(self):
		return self.caseID

	@property
	def getDes(self):
		return self.des

	@property
	def getUrl(self):
		return self.url

	@property
	def getMethod(self):
		return self.method

	@property
	def getData(self):
		return self.data

	@property
	def getExpect(self):
		return self.expect

	@property
	def getHeaderss(self):
		return self.headerss

class OperationExcel(OperationYaml):#2个类都需要实例化，所以需要继承
	def getSheet(self):
		'''获取sheet（一般只会用一个sheet，会从下标获取）'''
		workbook = xlrd.open_workbook(filePath('data','dangdang.xls'))
		return workbook.sheet_by_index(0)

	# @property
	# def getRows(self):
	# 	'''获取总共行数（可变）'''
	# 	return self.getSheet().nrows
	# @property#特性方法，调用时，无形参
	# def getCols(self):
	# 	'''获取总列（不变）'''
	# 	return self.getSheet().ncols

	def getValue(self,row,col):
		'''获取具体单元格数据'''
		return self.getSheet().cell_value(row,col)

	def getCaseID(self,row):
		return self.getValue(row=row,col=ExcelVarles().getCaseID)

	def getUrl(self,row):
		url=self.getValue(row=row, col=ExcelVarles().getUrl)
		dangEnvironment=utils.readConfig.getEnvironment()[0] #获取dangTest1环境
		if '{dang_environment}' in url:
			return str(url).replace('{dang_environment}',dangEnvironment)
		else:
			return url

	def getMethod(self,row):
		return self.getValue(row=row, col=ExcelVarles().getMethod)

	def getHeaderss(self, row):
		'''获先从excel获取到参数列key（getData）'''
		headerValue= self.getValue(row=row, col=ExcelVarles().getHeaderss)
		cookieValue = self.readDataValue(fileName='cookieText')['cookie']
		if '{Cookie}' in headerValue:
			return json.loads(str(headerValue).replace('{Cookie}',cookieValue))
		else:
			return headerValue

		# return self.getValue(row=row, col=ExcelVarles().getHeaderss)

	def getData(self,row):
		'''获先从excel获取到参数列key（getData）'''
		return self.getValue(row=row,col=ExcelVarles().getData)

	def getDataValue(self,row):
		'''获取请求参数（先从excel获取到参数列key（getData），再获取列的具体值dictConfig（））'''
		return self.readDataValue()[self.getData(row=row)]

	def getExpect(self,row):
		return self.getValue(row=row, col=ExcelVarles().getExpect)

if __name__ == '__main__':
	obj = OperationExcel()

	# print(obj.getValue(1,4))
	# print(obj.getDataValue(row=1))
	print(obj.getHeaderss(row=2))
	# print(obj.getUrl(row=2))
	# print(utils.readConfig.getEnvironment()[0])