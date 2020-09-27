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

class Weworlk(BaseApi):
    def __init__(self):
        self.token = Util().get_token()
        print(self.token)
        self.params["token"]= self.token

    def test_create(self, userid, name, mobile, department=None,*args,**kwargs):
        '''
        创建成员
        https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        :return:
        '''
        if department is None:
            #department = [1]
            department = "1"
        # request_body = {
        #     "userid": userid,
        #     "name": name,
        #     "alias": "jackzhang",
        #     "mobile": mobile,
        #     "department": department
        # }
        #ACCESS_TOKEN=self.token
        # print(ACCESS_TOKEN)
        # r=requests.post(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={ACCESS_TOKEN}",
        #               json=request_body)

        # data = {
        #     "method" : "post",
        #     "url"    :  f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={ACCESS_TOKEN}" ,
        #     "json"   :  {
        #         "userid": userid,
        #         "name": name,
        #         "alias": "jackzhang",
        #         "mobile": mobile,
        #         "department": department
        #     }
        # }
        self.params["userid"] = userid
        self.params["mobile"] = mobile
        self.params["name"] = name
        self.params["department"] = department
        with open("../api/wework.yaml", encoding="utf-8") as f:
            data=yaml.safe_load(f)
        return self.send(data["create"])


    def test_get(self, userid):
        '''
        获取成员
        https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        '''
        #r=requests.get(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}")
        #print(r.json())
        #return r.json()
        data = {
            "method" : "get",
            "url"   : f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}"
        }
        #print(self.send(data))
        return self.send(data)

    def test_update(self, userid, mobile, name="柯南", *args,**kwargs):
        '''
        更新成员
        https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN

        :return:
        '''
        request_body = {
                "userid": userid,
                "name": name,
                "mobile": mobile,
                **kwargs
        }
        data = {
            "method" : "post",
            "url"    : f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
            "json"  : request_body
        }
        #r = requests.post(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
        #                  json=request_body)
        #print(r.json())
        #return r.json

        return self.send(data)

    def test_delete(self,userid):
        '''
        删除成员
        https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        '''
        #r=requests.get(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}")
        #print(r.json())
        #return r.json()
        data = {
            "method" : "get" ,
            "url"    : f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}"

        }
        return  self.send(data)