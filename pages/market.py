import yaml
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.search import Search


class Market(BasePage):
    def goto_search(self):
        #self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        self.steps("../pages/market.yaml", 'goto_search')
        return Search(self.driver)