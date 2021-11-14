#!usr/bin/env python
# File_Name:test_token
# -*- coding:utf-8 -*-
# Author:Lins_369
from unittest import TestCase

from api_tests.token import Weixin


class TestWeixin(TestCase):
	def test_get_token(self):
		# print(Weixin.get_token())
		assert Weixin.get_token() != ""
