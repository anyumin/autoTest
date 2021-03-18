#!/user/bin/env python
# -*- coding:utf-8 -*-
# author:yumin An
import configparser
import os

def base_dir(filename=None):
	return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', filename)

def getEnvironment(environment='test_environment'):
	'''获取环境的配置'''
	list = []
	config = configparser.ConfigParser()
	config.read(base_dir('environmentText.ini'))
	dangTest1 = config.get(environment, 'dangTest1')
	lagouTest1 = config.get(environment, 'lagouTest1')
	list.append(dangTest1)
	list.append(lagouTest1)
	return list

def getMysql(environment='dang_mysql'):
	'''获取环境的配置'''
	dict = {}
	config = configparser.ConfigParser()
	config.read(base_dir('environmentText.ini'))
	dict["IP"]=config.get(environment, 'IP')
	dict["DB"]=config.get(environment, 'DB')
	dict["username"]=config.get(environment, 'username')
	dict["password"]=config.get(environment, 'password')
	return dict

print(getMysql()["IP"])