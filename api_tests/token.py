#!usr/bin/env python
# File_Name:token
# -*- coding:utf-8 -*-
# Author:Lins_369
import logging

import requests
import yaml


class Weixin:
	logging.basicConfig(level=logging.DEBUG)
	_token = ""

	@classmethod
	def get_token(cls):
		if len(cls._token) == 0:
			conf = yaml.load(open("weixin.yaml"), Loader=yaml.FullLoader)
			# logging.debug(conf["env"])
			r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
							 params={"corpid": conf["env"]["corp_id"], "corpsecret": conf["env"]["secret"]}).json()
			# print(r["access_token"])
			cls._token = r["access_token"]

		return cls._token
