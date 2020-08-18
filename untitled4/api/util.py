import  requests
class Util:
    def get_token(self):
        requests_params =  {
            "corpid": 'ww5ec2ae9af30fe1f4',
            "corpsecret": 'S8W26qDor05ykYGwPmB-TNEUOscqtIwMpr1TPqf2QJU'
        }
        r = requests.get(url="https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params=requests_params)
        #print(type(r.json()))
        #print(r.json())
        #print(r.json()['access_token'])
        m=r.json()['access_token']
        print(f'123----{m}')
        return r.json()['access_token']
        corpid = 'ww5ec2ae9af30fe1f4'
        secret = 'S8W26qDor05ykYGwPmB-TPJtmOPHv6FqjQLp5D6l5SY'
        #r=requests.get(url=f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={secret}")
        #两句话可以达到一样的效果
        r=requests.get(url="https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                       params=requests_params)
        #print(type(r.json()))
        #print(r.json())
        #print(r.json()['access_token'])

        return r.json()['access_token']
