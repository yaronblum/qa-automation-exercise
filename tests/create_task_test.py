import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement




@pytest.mark.usefixtures("chrome_driver_init")
class TestCreateTask:

    def inject_cookie(self):
        self.driver.get('https://app.connecteam.com/')
        self.driver.add_cookie({'name': 'session', 'value': '2|1:0|10:1639476584|7:session|48:MDg0Nzk0YzMtOWYyYi00OGNhLTk4YTUtMzg3NzMyMjJiY2Y3|2dd6ca9d422d63931445fcb225f0b8bbaa960d4a60adebe07a8bdc85e2a7b057', 'domain': '.app.connecteam.com'})
        self.driver.add_cookie({'name': '_spirit', 'value': 'ddc64e4e-0e59-44be-9704-8cac4a5a23bd', 'domain': '.app.connecteam.com'})

    def setup_method(self):
        pass

    def test_create_task(self):
        self.inject_cookie()
        url = 'https://app.connecteam.com/#/index/task-management/taskManagement'
        self.driver.get(url)
