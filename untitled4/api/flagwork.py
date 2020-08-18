import json
import re
import random
from time import sleep

import yaml
from filelock import FileLock


from requests import  request
import pytest
from api.util import Util
import  requests
from api.baseapi import BaseApi

class FlagWeworlk(BaseApi):
    def __init__(self):
        self.token = Util().get_token()
        print(self.token)
        self.params["token"]= self.token
        with open("../api/flagwork.yaml", encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

    def test_create(self, tagid, tagname):
        '''
        创建成员
        https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token=ACCESS_TOKEN
        :return:
        '''
        self.params["tagname"] = tagname
        self.params["tagid"] = tagid
        return self.send(self.data["create"])

    def test_get(self, tagid):
        '''
        获取成员
        https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token=ACCESS_TOKEN&tagid=TAGID
        :return:
        '''
        self.params["tagid"] = tagid
        return self.send(self.data["get"])

    def test_update(self, tagid, tagname):
        '''
        更新成员
        https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token=ACCESS_TOKEN

        :return:
        '''

        self.params["tagid"] = tagid
        self.params["tagname"] = tagname
        return self.send(self.data["update"])

    def test_delete(self,tagid, userlist,partylist):
        '''
        删除成员
        https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers?access_token=ACCESS_TOKEN
        :return:
        '''
        self.params["tagid"] = tagid
        self.params["userlist"] = userlist
        self.params["partylist"] = partylist

        return  self.send(self.data["delete"])