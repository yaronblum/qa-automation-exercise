import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from actions.home_screen import HomeScreen
from actions.careers_screen import CareersScreen


@pytest.mark.usefixtures('wait_until_web_page_is_loaded')
def test_submit_cv(home_screen_actions: HomeScreen, careers_screen_actions: CareersScreen, chrome_web_driver_base: WebDriver):
    home_screen_actions.scroll_to_bottom_of_web_page()
    home_screen_actions.tap_on_careers_footer()
    careers_screen_actions.find_and_tap_RD_sections()
    careers_screen_actions.iter_over_positions()

