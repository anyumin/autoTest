#!/user/bin/env python
# -*- coding:utf-8 -*-
# author:yumin An

import os

def filePath(fileDir='data',fileName='data.yaml'):
	return os.path.join(
		os.path.dirname(os.path.dirname(__file__)),fileDir,fileName)

# print(filePath('data','data.yaml'))
def writeContent(content,fileName):
	'''动态参数可以写到目标文件中'''
	with open(filePath(fileDir='data',fileName=fileName),"w") as f:
		f.write(str(content))

def readContent(fileName):
	'''可以从上面目标文件中读取到响应内容'''
	with open(filePath(fileDir='data',fileName=fileName),"r") as f:
		return f.read()

# writeContent(1,"testwe")
# print(readContent("testwe"))