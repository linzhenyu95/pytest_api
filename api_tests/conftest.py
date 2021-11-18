#!usr/bin/env python
# File_Name:conftest
# -*- coding:utf-8 -*-
# Author:Lins_369
import pytest

from api_tests.token import Weixin


@pytest.fixture(scope="session")
def token():
    return Weixin.get_new_token()
