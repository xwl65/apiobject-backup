from time import sleep
import pytest
from pages.app import App


class TestXueqiu:
    def setup(self):
        self.app = App()

    def test_market(self):
        self.app.start().goto_main().goto_market()


    @pytest.mark.parametrize("stock_name", ["阿里巴巴","京东"])
    def test_search(self, stock_name):

        search = self.app.start().goto_main().goto_market().goto_search()
        search.search(stock_name)
        assert search.is_choose(stock_name)




def wrapper(fun):
    def hello(*args, **kwargs):
        print("hello")
        fun(*args, **kwargs)
        print("good bye")
    return hello


@wrapper
def tmp():
    print("tmp")


def tmp1():
    print("tmp1")


def tmp2():
    print("hello")
    print("tmp2")
    print("good bye")

def tmp3(*args, **kwargs):
    print(*args)
    print(kwargs)

def test_tmp():
    # tmp()
    # wrapper(tmp1)()
    tmp3(10,20,a=10,b=10)
