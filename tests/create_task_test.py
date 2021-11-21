import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement




@pytest.mark.usefixtures("chrome_driver_init")
class TestCreateTask:

    def inject_cookie(self):
        self.driver.get('https://app.connecteam.com/')
        self.driver.add_cookie({'name': 'session', 'value': '2|1:0|10:1637512388|7:session|48:NDVhN2EyZjAtOWY4Ni00ODk1LTlkMGQtNmRlMTc1YjhhNjhh|9a6b06a59ba1f13d9ebcbcc269b8e5a2af54472228092bab66b6180fd6dbc82d', 'domain': '.app.connecteam.com'})
        self.driver.add_cookie({'name': '_spirit', 'value': 'bb4f8186-efbf-468f-b736-b7cab8b9afae', 'domain': '.app.connecteam.com'})

    def setup_method(self):
        pass

    def test_create_task(self):
        self.inject_cookie()
        url = 'https://app.connecteam.com/#/index/task-management/taskManagement'
        self.driver.get(url)
