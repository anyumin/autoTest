#!/user/bin/env python
# -*- coding:utf-8 -*-
# author:yumin An

import yaml
from common.public import filePath

class OperationYaml:
	def readYaml(self):
		with open(filePath(),'r',encoding="utf-8") as f:
			return list(yaml.safe_load_all(f))

	def readDataValue(self,fileDir='config',fileName='dangdang.yaml'):
		'''获取列的具体值dictConfig（）'''
		with open(filePath(fileDir=fileDir,fileName=fileName),'r',encoding="utf-8") as  f:
			return yaml.safe_load(f)

if __name__ == '__main__':
	obj = OperationYaml()
# 	for item in obj.readYaml():
# 		print(item)
# 	print(obj.readDataValue()["lagou_0003"])