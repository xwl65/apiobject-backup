import requests

from api.wework import Weworlk
class TestWework:
    def test_get_token(self):
        print(Weworlk().test_get("kenan8888"))

    def test_create(selt):
        print(Weworlk().test_create("kenan8888",'zhangbing',"13800000011"))

    def test_update(self):
        print(Weworlk().test_update("kenan8888","13900011234","wangwu"))

    def test_delete(self):
        print(Weworlk().test_delete("kenan8888"))


    def test_session(self):
        s= requests.session()

