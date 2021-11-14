#!usr/bin/env python
# File_Name:test_department
# -*- coding:utf-8 -*-
# Author:Lins_369
import datetime
import json
import logging

import pytest
import requests

from api_tests.token import Weixin


class TestDepartment:
    @classmethod
    def setup_class(cls):
        print("setup class")
        Weixin.get_token()

    # print(Weixin._token)
    def setup(self):
        print("setup")

    # def test_create(self):
    # 	data = {
    # 	   "name": "广州研发中心",
    # 	   "name_en": "RDGZ",
    # 	   "parentid": 1,
    # 	   "order": 1,
    # 	   "id": 2
    # 	}
    def test_create_deth(self):
        parentid = 1
        for i in range(5):
            data = {
                # datetime.datetime.now().timestamp() 生成唯一时间字符串
                "name": "第一工作小组_" + str(parentid) + str(datetime.datetime.now().timestamp()),
                "parentid": parentid
            }
            r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                              params={"access_token": Weixin.get_token()},
                              json=data,
                              # proxies={"http":"http://127.0.0.1:8080",
                              #           "https":"http://127.0.0.1:8080"},
                              # verify=False
                              ).json()
            logging.debug(r)
            parentid = r["id"]
            assert r["errcode"] == 0

    def test_create_name(self):
        data = {
            "name": "上海研发中心",
            "parentid": 1,
            "order": 1

        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                          params={"access_token": Weixin.get_token()},
                          json=data,
                          ).json()
        logging.debug(r)

    @pytest.mark.parametrize("name", ["いのー異能けんきゅー研究しょ所", "이력 연구소"])
    def test_create_order(self, name):
        data = {
            "name": name,
            "parentid": 1,
            "order": 1

        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                          params={"access_token": Weixin.get_token()},
                          json=data,
                          ).json()
        logging.debug(r)
        assert r["errcode"] == 0

    def test_get(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",
                         params={"access_token": Weixin.get_token()}).json()
        # logging.debug(r)
        logging.info(json.dumps(r, indent=2))
