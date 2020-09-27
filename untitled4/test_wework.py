
import json
import re
import random
from time import sleep
from filelock import FileLock

from requests import  request
import pytest
import  requests


def test_create_data():
    "userid,name,mobile"
    #data = [(str(random.randint(0,9999999)), "柯南",str(random.randint(13900000000,13999999999))) for x in range(10)]
    #print(data)
    '''生成器 可以生成数据，我们现在使用的列表'''
    #为防止在并行运行过程中出现产生相同的数据，可以做如下优化
    #"139%18d"%x 通过补0，保证只有8个数字，
    data = [("kenanxx" + str(x), "kenan", "139%08d"%x)  for x in range(20)]
    print(data)
    return data

class TestWework:
    '''
            获取token

            corpid=ww5ec2ae9af30fe1f4

            requests.get(url="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid='corpid'&corpsecret=JD8hNLJl8lcIakqQLuozS9PsS7WSbS911bX8HNoP2Sw")

            '''
    #并行运行的时候，会创建多个session。如果运行100次用例，那么session就会多次运行。采取文件锁的形式可以解决这个问题。可以通过如下代码解决
    @pytest.fixture(scope="session")
    def token(self, tmp_path_factory, worker_id):
        def get_token():
            requests_params = {
                "corpid": 'ww5ec2ae9af30fe1f4',
                "corpsecret": 'S8W26qDor05ykYGwPmB-TNEUOscqtIwMpr1TPqf2QJU'
            }
            r = requests.get(url="https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                             params=requests_params)

            return r.json()['access_token']
        print('---99999-')
        print(worker_id)
        print('tmp')
        print(tmp_path_factory)
        if not worker_id:
            return get_token()
        root_tmp_dir = tmp_path_factory.getbasetemp().parent
        print('root_tmp_dir')
        print(root_tmp_dir)
        print('tmp_path_factory')
        print(tmp_path_factory)
        fn = root_tmp_dir / "data.json"
        print(f'fn{fn}')
        #获取token
        with FileLock(str(fn) + ".lock"):
            if fn.is_file():
                data = json.loads(fn.read_text())
                print(f'{data}date')
            else:
                data = get_token()
                fn.write_text(json.dumps(data))
        return data


    def test_get_token(self):
        requests_params =  {
            "corpid": 'ww5ec2ae9af30fe1f4',
            "corpsecret": 'S8W26qDor05ykYGwPmB-TNEUOscqtIwMpr1TPqf2QJU'
        }
        r = requests.get(url="https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params=requests_params)
        print(type(r.json()))
        print(r.json())
        print(r.json()['access_token'])
        return r.json()['access_token']
        corpid = 'ww5ec2ae9af30fe1f4'
        secret = 'S8W26qDor05ykYGwPmB-TNEUOscqtIwMpr1TPqf2QJU'
        #r=requests.get(url=f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={secret}")
        #两句话可以达到一样的效果
        r=requests.get(url="https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                       params=requests_params)
        print(type(r.json()))
        print(r.json())
        print(r.json()['access_token'])
        return r.json()['access_token']


    def test_create(self, token, userid, name, mobile, department=None,):
        '''
        创建成员
        https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        :return:
        '''
        if department is None:
            department = [1]
        request_body = {
            "userid": userid,
            "name": name,
            "alias": "jackzhang",
            "mobile": mobile,
            "department": department,
        }
        ACCESS_TOKEN=token
        print('------777777-----')
        print(ACCESS_TOKEN)
        r=requests.post(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={ACCESS_TOKEN}",
                      json=request_body)
        print(r.json())
        return r.json()


    def test_get(self,token, userid):
        '''
        获取成员
        https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        '''
        r=requests.get(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}")
        print(r.json())
        return r.json()

    def test_update(self,token, userid, mobile, name="柯南", *args,**kwargs):
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

        r = requests.post(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}",
                          json=request_body)
        print(r.json())
        return r.json()

    def test_delete(self,token,userid):
        '''
        删除成员
        https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        '''
        r=requests.get(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={userid}")
        print(r.json())
        return r.json()


    @pytest.mark.parametrize("userid, name, mobile", test_create_data())
    def test_wework(self,token, userid, name, mobile):

        '''
        整体测试

        :return:
        '''
        #userid = "kenan123"
        #name = "柯南"
        #mobile = "13900000000"

        try:
            assert "created" == self.test_create(token,userid,name,mobile)["errmsg"]
        except AssertionError as e:
            if "mobile existed" in e.__str__():
                print(e)
                print("6666-------")
                re_userid =re.findall(":(.*)'$", e.__str__())[0]
                print(re_userid)
                print(123)
                self.test_delete(token,re_userid)
                assert "created" == self.test_create(token, userid, name, mobile)["errmsg"]
        assert name == self.test_get(token, userid)["name"]
        print(mobile)
        print("------555555------------")
        assert "updated" == self.test_update(token, userid,mobile,  name="柯南5555")["errmsg"]
        print(mobile)
        assert "柯南5555" == self.test_get(token, userid)["name"]

        assert "deleted" == self.test_delete(token, userid)["errmsg"]
        assert 60111 == self.test_get(token, userid)["errcode"]

