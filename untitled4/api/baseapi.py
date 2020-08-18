import requests
import json
class BaseApi:
  params = {}
  def send(self, data):
    raw_data = json.dumps(data)
    for key, value in self.params.items():
      raw_data = raw_data.replace("${" + key + "}", value)
    print(123456)
    print(raw_data)
    data = json.loads(raw_data)
    return requests.request(**data).json()




def test_dict():
    a = {"kk" : 10, "ff":20}
    def tmp (kk,ff):
        print(kk)
        print(ff)
    tmp(**a)
