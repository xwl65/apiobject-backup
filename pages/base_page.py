import json
import copy
import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.handle_black import handle_black



class BasePage:
    _black_list = [
        (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")
    ]
    _max_err_num = 3
    _error_num = 0
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self.driver = driver
    #调用截图
    def screenshot(self,path):
        self.driver.save_screenshot(path)
    @handle_black
    def find(self, by, locator=None):
        if locator is None:
            result = self.driver.find_element(*by)
        else:
            print(locator)
            result = self.driver.find_element(by, locator)
        return result

    def finds(self, by, locator=None):
        if locator is None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by, locator)

    def set_implicitly_wait(self, second):
        self.driver.implicitly_wait(second)

    def steps(self, path, name):
        with open(path, encoding="utf-8") as f:
            steps = yaml.safe_load(f)
        #解析yaml文件中的变量
        #将python的形式转换位jason
        #将storck_name变为alibaba
        #具体例子可见test_yaml
        #将steps转换为字符串，因为jeson不支持字典

        print(self._params)
        raw = json.dumps(steps)
        print(raw)
        for key, value in self._params.items():
            raw = raw.replace('${' + key + '}', value)
        steps = json.loads(raw)
        print(steps)

        for step in steps[name]:
            if "action" in step.keys():
                action = step["action"]
                if "click" == action:
                    self.find(step["by"], step["locator"]).click()

                    print(1,23,step["locator"])
                if "send" == action:
                    self.find(step["by"], step["locator"]).send_keys(step["value"])
                    print(2,step["locator"])
                if "len > 0" == action:
                    eles = self.finds(step["by"], step["locator"])
                    print(3,step["locator"])
                    return len(eles) > 0

    def back(self):
        self.driver.back()