#!/user/bin/env python
# -*- coding:utf-8 -*-
# author:yumin An

from base.method import Requests
import requests

re = Requests()
r = re.request(
	url ="https://passport.lagou.com/login/login.json",
	method='get',
	params = {'jsoncallback': 'jQuery111306939998565532908_1615971072665', 'isValidate': True, 'username': 13136166390, 'request_form_verifyCode': None, 'phoneVerificationCode': 437181, 'autoPhoneVerificationCode': None, 'countryCode': '0086', 'challenge': 111, '_': 1615971072669},
	headers = {"Content-Type": "application/x-www-form-urlencoded"},
	allow_redirects=False
)
# print(requests.utils.dict_from_cookiejar(r.cookies))
print(r.cookies.get_dict())