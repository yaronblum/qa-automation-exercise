import os
from typing import List

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def chrome_driver_init(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--kiosk")
    if "SELENIUM_HUB_URL" in os.environ:
        chrome_driver = webdriver.Remote(
            command_executor=os.environ["SELENIUM_HUB_URL"],
            options=options,
        )
    else:
        chrome_driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()


