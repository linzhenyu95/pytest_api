#!usr/bin/env python
# File_Name:test_user
# -*- coding:utf-8 -*-
# Author:Lins_369
import json
import logging
import time

import pystache
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

    # 模板创建，模板替换
    def test_create_template(self):
        print(pystache.render("hello {{name}} {{#has}} world {{value}}  {{/has}}",
                              {"name": "lins",
                               "has": [{"value": 1}, {"value": 2}, {"value": 3}],
                               }))

    def test_create_by_template(self):
        uid = "seveniruby_" + str(time.time())
        mobile = str(time.time()).replace(".", "")[0:11]
        data = str(self.get_user({
            "name": uid,
            "title": "校长",
            "email": "2222@qq.com",
            "mobile": mobile
        }))
        data = data.encode("UTF-8")

        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                          params={"access_token": Weixin.get_token()},
                          data=data,
                          headers={"content-tyoe": "application/json;charset=UTF-8"}
                          ).json()
        logging.info(r)
        # print(r)
        assert r["errcode"] == 0

    def test_list(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
                         params={"access_token": Weixin.get_token(),
                                 "department_id": [23]}).json()
        logging.debug(r)
        logging.info(json.dumps(r, indent=2))
        # print(r)

        # assert r["errcode"]==0

    def get_user(self, dict):
        template = "".join(open("user_create.json", encoding='utf-8').readlines())
        logging.debug(template)
        return pystache.render(template, dict)

    def test_get_user(self):
        logging.debug(self.get_user({"name": "seveniruby", "title": "校长", "email": "1@.com"}))
