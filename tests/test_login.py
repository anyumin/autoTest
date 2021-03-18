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
	print(r.text)
if __name__ == '__main__':
    pytest.main("-s","-v","test_login.py")




