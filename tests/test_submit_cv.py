import time

import pytest


@pytest.mark.usefixtures("chrome_web_driver_base")
class TestSubmitCv:
    def test_submit_cv(self, chrome_web_driver_base):
        chrome_web_driver_base.get("https://connecteam.com/")
        time.sleep(5)
