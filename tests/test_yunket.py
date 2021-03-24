#!/user/bin/env python
# -*- coding:utf-8 -*-
# author:yumin An

import pytest
from base.method import Requests
from utils.operationExcel import OperationExcel
from utils.getHeaders import getHeaders


class Testyunket:
	req = Requests()
	excel = OperationExcel()
	global header
	header={'Cookie':'EDUWEBDEVICE=eb652b120b914846b23c63beb06c277b; EDU-YKT-MODULE_GLOBAL_PRIVACY_DIALOG=true; 1140087299=1140087299; OUTFOX_SEARCH_USER_ID_NCOO=249788378.68942502; UM_distinctid=17810f1747c959-08e92f47030c8c-53e356a-e1000-17810f1747da09; eds_utm=eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly93d3cuYmFpZHUuY29tL2xpbms/dXJsPVR4enQ0NmhqY3JwdEpmTUhhUXVJZkdfaC1sSjlvSFFWSUk4OWF1VFotNTMmd2Q9JmVxaWQ9YmIwODBiNmMwMDBmOGVhNzAwMDAwMDA1NjA0ZmViNDc=; __utmz=129633230.1615850317.54.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=129633230; hasVolume=true; _ntes_nnid=71d171bc2f56de60a5827b954bb84ede,1616046781328; _ntes_nuid=71d171bc2f56de60a5827b954bb84ede; mail_psc_fingerprint=cc3af4f76d860b369db5e0c817a013c9; sideBarPost=1264; videoResolutionType=3; videoVolume=0.75; videoRate=1.25; nts_mail_user=anyumin2021@163.com:-1:1; __utma=129633230.358953019.1614867963.1616304865.1616395587.72; hb_MA-BFF5-63705950A31C_source=study.163.com; utm="eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly9rZS5zdHVkeS4xNjMuY29tL2NvdXJzZS9kZXRhaWwvMTAwMDc4MTM1P1BkdD15ZGtXZWImaW5Mb2M9d2ViX3NzX3NzcmM="; NTESSTUDYSI=5f57b893e5bf4efd970f60ba47c5a837; YD_SC_SID=1B28EE4C7F26457ABA09653964BDF7B8; NETS_utid=PLrpZOUlFduBQhIwDfKS8gY42U7dHZ8I; NTES_YD_SESS=FKppMFAiyqMdTh7Zl61_vM375uQ8iAPbF.LHJNbrdLNKkrW0kCD17ofnPN7ODsNL6w09kgGT1ODR_RiWg00A25QTeGeIzaVZHdhp5vOURcsaR8zG4pwxFu81rRoxopqUKf0pqwnJnafYlU1bLgIqnGF4F0iqYSItGK7dLyxSgJBS1qxNZLikxhMvXpjySleKu8hdei68daWPXlcwvFL9rxYlHE.dtzIoRFC1ryC55.XiV; NTES_YD_PASSPORT=k61Fbq7T8NGD05pD6Jp6iImr3X30dpgOtbsIygXeYC_U7LHE7Muc9bXpJT9Ru0TdrjEI7GfDcRu3x.XMjH3nGHAs_jJT0fLK65X5hjjtGZL6J8uWscDHV5D4FLArBu1y_dHbzxP.FueHZGD_X08gBUXMBXdAYau2my8OiOL72CIzQ8gCiihDs.z8MEHgfZfneJzaCRBbD2BUsiS5AfMUZam2z; S_INFO=1616395991|0|3&80##|13136166390; P_INFO=13136166390|1616395991|1|study|00&99|zhj&1615944585&study_client#zhj&330100#10#0#0|&0|null|13136166390; STUDY_INFO="yd.9e450ffdea50401da@163.com|8|1140087299|1616395991533"; STUDY_SESS="4lkUrV0rYQVkxP9TTAmtfR+osO3Q8sbuRISN7SjBO/T8OE5DU0SfMShyeZrB/dL5F1RaXEkOxmcSgbELZrqgeJkGKHYKN/z+Oh6H1wOxdiIB3NV+fRXRmH/WofdLjD7h4oJY+QrYmk3vnbSTDlLrRNZ/NiyCQaEopUqZDZ2gxCkLhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="ds+yImgh5IpYpKxjPosiztPHxI1+N8tbqUONgMbLOoUsD3BBJXto75LdDkyiUJuV9EgMdSmdzomgVhGH6xTtKY1QayMWVQGifwrtWjYqZ9FsVwMHwtOnRDKFheN1TkcYRjyYDNEf0Dhr6F05Je6ySL/lLvgp7Lwd68Chfp2NLWRUySU1z8tua5AIWXI3WQ2K+34u5LQy3CEFkgM6BUwlp12V/BfAUihs+RTZV3Qq4l3ZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; DICT_SESS=v2|GA73zVulEBeZhfgz0HQuRl50fPKhfe406LhHOGO4PFRqZOfgyRLqy0QLhM6z64pz0Of6Mgz0LQy0kfOMJK0HpL0YGOLkm64eFR; DICT_LOGIN=1||1616395991585; NETEASE_WDA_UID=1140087299#|#1525503558748; NTES_STUDY_YUNXIN_ACCID=s-1140087299; NTES_STUDY_YUNXIN_TOKEN=0795677da5435c59a6da72305346c45e; STUDY_UUID=ff1c373b-c6a1-4bfb-b742-20a6a6749454; __utmb=129633230.31.8.1616396146409',
	    'content-type':'application/json','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
	# @pytest.fixture()
	def test_yunket_0001(self):
		'''模糊查询，根据字符串”python'''
		cookiess = getHeaders.readheader()['yunCookie']
		response = self.req.request(
			url=getHeaders.getYunUrl(uri="/j/search/suggestions/courses.json"),
			method="post",
			# headers=header,
			headers=getHeaders.getJsonHeader(cookiess),
			params=self.excel.getDataValue(row=5)
		)
		assert response.json()['code']==0
		assert response.json()['result'][0]['productName']=="Python五项全能班·10班"
		assert response.status_code==200
		return response.json()

	# def test_yunket_0002(self,tmpdir,test_yunket_0001):
	# 	'''根据课程id查询'''
	# 	f=tmpdir.join("course.txt")
	# 	res=test_yunket_0001['result'][0]['courseId']
	# 	f.write(res)
	# 	response = self.req.request(
	# 		url=self.excel.getUrl(row=6),
	# 		method=self.excel.getMethod(row=6),
	# 		# headers=self.excel.getHeaderss(row=5),
	# 		headers=header,
	# 		params={"courseId":f.read()}
	# 	)
	# 	assert response.json()['status']==0
	#
	# @pytest.fixture()
	# def test_yunket_0003(self,tmpdir,test_yunket_0001):
	# 	f=tmpdir.join("productId.txt")
	# 	f.write(test_yunket_0001['result'][0]['productId'])
	# 	response = self.req.request(
	# 		url=self.excel.getUrl(row=7),
	# 		method=self.excel.getMethod(row=7),
	# 		# headers=self.excel.getHeaderss(row=5),
	# 		headers=header,
	# 		params={"productId":f.read()}
	# 	)
	# 	# assert response.json()['message']=="ok"
	# 	return response.json()
	#
	# def test_test4(self,tmpdir,test_yunket_0001,test_yunket_0003):
	# 	'''测试一个需要多个用例的出参'''
	# 	f3=tmpdir.join("testss.txt")
	# 	f3.write(test_yunket_0003)
	# 	f1=tmpdir.join("f1test.txt")
	# 	f1.write(test_yunket_0001)
	# 	print(f"f1:{f1.read()}")
	# 	print(f"f3:{f3.read()}")




if __name__ == '__main__':
    pytest.main("-s,-v,test.yunket.py")