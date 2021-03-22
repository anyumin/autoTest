#!/user/bin/env python
# -*- coding:utf-8 -*-
# author:yumin An
import requests
import pytest
from tests.test_loginUtils import login

class Testfix:

	def test_dangdang02(self,tmpdir,login):
		f = tmpdir.join("cookiess.txt")
		f.write(login)
		f1 = tmpdir.join("test.txt")
		f1.write("9")
		r = requests.get(
			url="http://localhost:8080/dangdang/cart/cartBuy",
			headers={"Cookie": f.read()},
			params={"id": f1.read()})
		print(f"结果：{f1.read()}")

	# def test_dag3(self,tmpdir,login):


if __name__ == '__main__':
	pytest.main("-s, -v, test_testfix.py")