#!/user/bin/env python
# -*- coding:utf-8 -*-
# author:yumin An

import pymysql
import utils.readConfig
class mysqlUtils(object):
	def connMysql(self):
		dict = utils.readConfig.getMysql()
		conn = pymysql.connect(
			host=dict["IP"],
			user=dict["username"],
			passwd=dict["password"],
			db=dict["DB"])
		return conn

	def readSql(self,mysql,params=None):
		try:
			conn = self.connMysql()
			cur = conn.cursor()
		except Exception:
			return Exception.args
		else:
			cur.execute(mysql,params)
			data = cur.fetchall()
			db = [item for item in data]  # 列表推导式：相当于for循环
			return db
		finally:
			cur.close()
			conn.close()

	def writSql(self,mysql,params=None):
		try:
			conn = self.connMysql()
			cur = conn.cursor()
		except Exception:
			return Exception.args
		else:
			cur.executemany(mysql,params)
			conn.commit()
		finally:
			cur.close()
			conn.close()


if __name__ == '__main__':
	sql = mysqlUtils()
	print(sql.readSql(mysql="select * from d_product limit 5"))
	# print(sql.connMysql())