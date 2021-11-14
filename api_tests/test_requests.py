#!usr/bin/env python
# File_Name:test_requests
# -*- coding:utf-8 -*-
# Author:Lins_369
import json
import logging

import jsonpath
import requests


class TestRequests(object):
	logging.basicConfig(level=logging.INFO,
						format='%(asctime)s %(filename)s %(levelname)s %(message)s',
						datefmt='%a %d %b %Y %H:%M:%S',
						filename='my.log',
						filemode='w')
	# logging.getLogger().setLevel(logging.INFO)
	url = "https://testerhome.com/api/v3/topics.json?limit=2"

	def test_get(self):
		res = requests.get(self.url)
		logging.info(res)
		logging.info(res.text)
		logging.info(json.dumps(res.json(), indent=2))

	def test_post(self):
		res = requests.post(self.url, params={"a": 1, "b": "string cortent"},
							headers={"a": "a1", "b": "b2"},
							proxies={"https": "http://127.0.0.1:28796", "http": "http://127.0.0.1:28796"}, verify=False)
		logging.info(res.url)
		logging.info(res.text)
		logging.info(json.dumps(res.json(), indent=2))

	# def test_cookies(self):
	# 	res = requests.get("http://121.4.49.239/cookies", cookies={"a": "1", "b": "string"})
	# 	# print(res.text)
	# 	logging.info(res.text)

	def test_baidu(self):
		url = 'https://www.baidu.com/s?ie=utf-8&csq=1&pstg=20&mod=2&isbd=1&cqid=ace34d0d0014c3f1&istc=1096&ver=RAoaHwVXOr4ajeyf5KWGz39Z2rN8XSCUEIK&chk=617a8754&isid=b935182e0000d8e5&ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=logging%E6%A8%A1%E5%9D%97%E6%B2%A1%E6%9C%89%E7%94%9F%E6%95%88&oq=logging%25E6%25A8%25A1%25E5%259D%2597%25E6%25B2%25A1%25E6%259C%2589%25E7%2594%259F%25E6%2595%2588&rsv_pq=b935182e0000d8e5&rsv_t=93a8PZcyNIBcHcLBdSoKsvtNm%2BpMcgU0feY0t8HzbIaYs5kE0oPvddXsGaA&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_btype=t&bs=logging%E6%A8%A1%E5%9D%97%E6%B2%A1%E6%9C%89%E7%94%9F%E6%95%88&f4s=1&_ck=161278.1.137.54.14.667.29&isnop=0&rsv_stat=-2&rsv_bp=1'
		res = requests.get(url)
		logging.info(res.text)

	# def test_login(self):
	# 	url =

	def test_cookies(self):
		r = requests.get("http://121.4.49.239:6001/#/Cookies",
						 cookies={"a": "2", "b": "string"})
		# print(r.text)
		logging.info(r.text)

	def test_baidu_search(self):
		r = requests.get("https://api.vc.bilibili.com/session_svr/v1/session_svr/get_sessions",
						 params={'session_type': '3', 'size': '1', 'group_fold': '1', 'unfollow_fold': '0',
								 'sort_rule': '1', 'build': '0', 'mobi_app': 'web'},
						 headers={'Content-Type': 'application/json'},
						 cookies={"b_ut": "-1", "i-wanna-go-back": "-1",
								  "_uuid": "1149B05F-2E9F-8DE9-133D-C774831C198860340infoc",
								  "buvid3": "2C1578FC-031E-4040-8F9E-9BF94B2C2B9A148820infoc", "blackside_state": "1",
								  "rpdid": "|(J~k))|~uJm0J'uYJkYlRYu)",
								  "fingerprint": "eb76027657e9ab7f675cd2cf536f702a",
								  "buvid_fp": "58D66863-CFD8-4B1E-940D-86809404AA22148807infoc",
								  "buvid_fp_plain": "58D66863-CFD8-4B1E-940D-86809404AA22148807infoc",
								  "CURRENT_QUALITY": "116", "DedeUserID": "687581",
								  "DedeUserID__ckMd5": "45def604d1354063",
								  "SESSDATA": "d554f591%2C1648208497%2C5d068*91",
								  "bili_jct": "645c253262238f03911407536d158f55", "LIVE_BUVID": "AUTO2316327524896087",
								  "video_page_version": "v_new_home_4", "PVID": "1",
								  "CURRENT_BLACKGAP": "0", "CURRENT_FNVAL": "976",
								  "bp_video_offset_687581": "591811339088404000",
								  "bp_t_offset_687581": "591814147997042666",
								  "innersign": "1"})

		logging.info(json.dumps(r.json(), indent=2))
		print(jsonpath.jsonpath(r.json(), "$.data.session_list[0].group_name"))
		# logging.info(json.dumps(),)
		# print(r.json())
		print(jsonpath.jsonpath(r.json(), "$.data.has_more"))
		assert r.json()['data']['has_more'] == 1
