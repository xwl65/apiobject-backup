import requests
import pytest
from api.flagwork import FlagWeworlk

def test_create_data():
    "tagid,tagname"

    '''生成器 可以生成数据，使用列表'''

    data = [("kenanxx" + str(x), "kenan" + str(x))  for x in range(20)]
    return data


class TestWework:
    def test_get_token(self):
        print(FlagWeworlk().test_get("kenan8888"))

    @pytest.mark.parametrize("tagid, tagname", test_create_data())
    def test_flag_create(self,tagid, tagname):
        '''
                整体测试

                :return:
                '''
        print(FlagWeworlk().test_create(tagid=tagid,tagname=tagname))

    def test_flag_get(self):
        print(FlagWeworlk().test_get("12"))

    def test_flag_delete(self):
        print(FlagWeworlk().test_delete("12"))

    def test_flag_update(self):
        print(FlagWeworlk().test_update("12", "xi"))




