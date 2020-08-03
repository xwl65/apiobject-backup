import yaml
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Search(BasePage):
    def search(self, stock_name):
        #参数传递
        self._params["stock_name"] = stock_name
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("阿里巴巴")
        # self.find(By.XPATH, "//*[@text='阿里巴巴-SW' and @resource-id='com.xueqiu.android:id/name']").click()
        # self.find(By.XPATH,
        #f"//*[contains(@resource-id, 'stock_item_container')]//*[@text='{stock_name}']/../..//*[@text='加自选']").click()
        self.steps("../pages/search1.yaml", 'search')

    def is_choose(self, stock_name):
        # eles = self.finds(By.XPATH,
        #                   f"//*[contains(@resource-id, 'stock_item_container')]//*[@text='{stock_name}']/../..//*[@text='已添加']")
        # return len(eles) > 0
        #下面这句话的意思是将stock_name设置为全局变量
        self._params["stock_name"] = stock_name
        return self.steps("../pages/search2.yaml", 'is_choose')
