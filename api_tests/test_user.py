#!usr/bin/env python
# File_Name:test_user
# -*- coding:utf-8 -*-
# Author:Lins_369
import json
import logging
import time

import requests

from api_tests.test_token import Weixin


class TestUser:
    depart_id = 23
    logging.getLogger().setLevel(logging.INFO)

    @classmethod
    def setup_class(cls):
        # todo:create depart
        pass

    def test_create_user(self):
        # uid=str(datetime.datetime.now().timestamp())
        uid = str(time.time())
        data = {"userid": "jiejie",
                "name": "杰杰",
                "department": [self.depart_id],
                "email": uid + "@qq.com"}
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                          params={"access_token": Weixin.get_token()},
                          json=data).json()
        logging.debug(r)
        print(r)
        assert r["errcode"] == 0

    # 模板创建
    def test_create_tem(self):
        data = {

        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                          params={"access_token": Weixin.get_token()},
                          json=data).json()
        logging.debug(r)
        print(r)
        assert r["errcode"] == 0

    def test_list(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
                         params={"access_token": Weixin.get_token(),
                                 "department_id": [23]}).json()
        logging.debug(r)
        logging.info(json.dumps(r, indent=2))
        # print(r)

        # assert r["errcode"]==0
