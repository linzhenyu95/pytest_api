#!usr/bin/env python
# File_Name:test_user
# -*- coding:utf-8 -*-
# Author:Lins_369
import logging
import time

import requests

from api_tests.test_token import Weixin


class TestUser:
    depart_id = 1

    @classmethod
    def setup_class(cls):
        # todo:create depart
        pass

    def test_create_user(self):
        # uid=str(datetime.datetime.now().timestamp())
        uid = str(time.time())
        data = {"userid": uid,
                "name": uid,
                "department": [self.depart_id],
                "eamil": "123456@qq.com"}
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                          params={"access_token": Weixin.get_token()},
                          json=data).json
        logging.debug(r)
        print(r)
