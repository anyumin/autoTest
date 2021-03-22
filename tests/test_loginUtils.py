#!/user/bin/env python
# -*- coding:utf-8 -*-
# author:yumin An

import pytest
import requests

@pytest.fixture()
def login():
	return "JSESSIONID=25A7DD8E294B88923C935F3136BD793A; Pycharm-2f240916=3a883774-401b-45c8-904e-7658458e89cd"

def test_dangdang_0001(tmpdir,login):
	f = tmpdir.join("cookiess.txt")
	f.write(login)
	r = requests.get(
		url="http://localhost:8080/dangdang/cart/cartBuy",
		headers={"Cookie":f.read()},
		params={"id":7}	)

	f = tmpdir.join("cookiess.txt")

if __name__ == '__main__':
    pytest.main("-s","-v","test_loginUtils.py")