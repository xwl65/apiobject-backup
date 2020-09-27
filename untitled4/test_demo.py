import json
import random
import requests
import pystache
from jsonpath import jsonpath
from requests_xml import XMLSession
from hamcrest import  *
from jsonschema import validate
from requests.auth import HTTPBasicAuth
import xml.etree.ElementInclude


def test_create_data():
    "userid,name,mobile"
    data = [(str(random.randint(0, 9999999)), "柯南", str(random.randint(13900000000, 13999999999))) for ix in
            range(3)]
    print(data)

class TestDemo:
    def test_get(self):
        r= requests.get('http://httpbin.testing-studio.com/get')

        print(r)
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert  r.status_code == 200

    def test_query(self):
        payload={
            "level": 1,
            "name" : "seveniruby"
        }
        r = requests.get('http://httpbin.testing-studio.com/get',params=payload)
        print(r.text)
        assert r.status_code == 200



    def test_post_form(self):
        payload={
            "level": 1,
            "name" : "seveniruby"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_header(self):
        r = requests.get('http://httpbin.testing-studio.com/get', headers={"h": "header-demo"})
        print(r.text)
        print(r.status_code)
        print(r.json())
        assert r.status_code == 200
        assert r.json()['headers']["H"]  == 'header-demo'


    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        assert r.json()['json']['level']  == 1


        # 如果又一些特别复杂的json文件，特别长，可以将一些文件保存到文件里面，然后利用模板技术来解析数据
         #可以使用mustache，freemaker等工具解析
    def test_xml(self):
         #由于requests没有封装xml，因此需要在编写脚本之前需要先添加如下语句
           #headers = {'Content-Type':'application/xml'} #加上这么一句才能对xml进行处理
           #可以应用于对一些特别长的文本进行操作
        r=pystache.render(
            'Hi{{person}!}',
            {'person':'seveniruby'}
            )
        print(r)

    # json path 断言
    def test_hogwarts_json(self):
        r = requests.get('http://home.testing-studio.com/categories.json')
        print(r.text)
        print(r.status_code)
        print(r.json())
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == '社区治理'
        #使用jsonpath将assert内容缩短
        #jsonpath里面传递过来的必须得是json的数据
        assert jsonpath(r.json(), '$..name')[0] == "社区治理"


#xpath断言
    def test_xpath(self):
        session = XMLSession()
        r = session.get('http://home.testing-studio.com/categories')
        item = r.text
        print(item)


#除了第三方的一些库之外，还有python自己的库可以解析
#如import xml.etree.ElementInclude
#对于一些非常复杂的断言的时候可以使用hamcrest
    def test_hamcrest(self):
        r = requests.get('http://home.testing-studio.com/categories.json')
        print(r.text)
        print(r.status_code)
        print(r.json())
        assert r.status_code == 200
        assert_that( r.json()['category_list']['categories'][0]['name'], equal_to('社区治理') )
        # 使用jsonpath将assert内容缩短
        # jsonpath里面传递过来的必须得是json的数据
        assert jsonpath(r.json(), '$..name')[0] == "社区治理"

#shema校验
#除了hamcrest进行比对之外，还有schema进行断言
    def test_get_login_jsonschema(self):
        url = 'https://testerhome.com/api/v3/topics.json'
        data = requests.get(url,params={'limit': '2'}).json()
        schema = json.load(open("topic_schema.json"))
        validate(data, schema=schema)

    def test_demo(self):
        url='https://httpbin.testing-studio.com/cookies'
        header = {"Cookie": 'hogwarts=shcool',
                  "User-Agent": "hogwarts" }
        cookies={"hogwarts": "shcool"}
        r=requests.get(url=url, headers=header, cookies=cookies)
        print(r.request.headers)
#传递cookies有多种模式
    def test_oauth(self):
        r= requests.get(url= "https://httpbin.testing-studio.com/basic-auth/banana/123",
                        auth= HTTPBasicAuth("banana", "123"))
        print(r)


    def test_Work(self):

        r = requests.get(url=' https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww5ec2ae9af30fe1f4&corpsecret=JD8hNLJl8lcIakqQLuozS9PsS7WSbS911bX8HNoP2Sw')

        #print(r.json())
        #return r.json()['access_token']
        request_body = {
            "userid": "zhangsan",
            "name": "张三",
            "alias": "jackzhang",
            "mobile": "+86 13800000000",
            "department": [1, 2],
        }
        ACCESS_TOKEN = r.json()['access_token']
        m = requests.post(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={ACCESS_TOKEN}",
                          json=request_body)
        print(m.json())


    def test_create(self):

        request_body= {
            "userid": "zhangsan",
            "name": "张三",
            "alias": "jackzhang",
            "mobile": "+86 13800000000",
            "department": [1, 2],
        }
        ACCESS_TOKEN = self.test_Work()
        r=requests.post(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={ACCESS_TOKEN}", json= request_body )
        print(r.json())


