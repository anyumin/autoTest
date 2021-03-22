#!/user/bin/env python
# -*- coding:utf-8 -*-
# author:yumin An

import pytest
import json
from base.method import Requests
from utils.operationYaml import OperationYaml
import  pytest

obj = Requests()
objYaml = OperationYaml()

@pytest.mark.parametrize('datas',objYaml.readYaml())
def test_login(datas):
	# print(datas)
	r = obj.post(
		url= datas['url'],
		data = datas['data'])
	# assert  dataLogin['except'] in json.dumps(r.json(),ensure_ascii=False)
	print(r.json)
if __name__ == '__main__':
	pytest.main("-s","-v","test_login.py") #-v显示运行的函数,-s显示内部的打印信息

	# pytest.main(["-s", "-v", "test_login.py", "--alluredir", "./report/result"])
	# import subprocess
	# subprocess.call('allure generate report/result/ -o report/html --clean', shell=True)
	# subprocess.call('allure open -h 127.0.0.1 -p  8188 ./report/html', shell=True)



