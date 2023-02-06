import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait

from infra.logger import logger
from data.common import Common
from data.home_screen import HomeScreen as HomeScreenData

from actions.home_screen import HomeScreen as HomeScreenActions
from actions.careers_screen import CareersScreen as CareersScreenActions


@pytest.fixture(scope='session')
def chrome_web_driver_base():
    logger.info('Launching Chrome-Driver')
    options = webdriver.ChromeOptions()
    chrome_driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    chrome_driver.delete_all_cookies()
    chrome_driver.maximize_window()

    yield chrome_driver

    logger.info('Killing Chrome-Driver')
    chrome_driver.quit()


@pytest.fixture
def wait_until_web_page_is_loaded(chrome_web_driver_base):
    logger.info('waiting for until webpage is loaded')
    chrome_web_driver_base.get(Common.connect_team_web_page)
    try:
        WebDriverWait(driver=chrome_web_driver_base, timeout=10).until(
            lambda d: d.find_element_by_class_name(HomeScreenData.connect_team_logo_class_name)
        )
    except TimeoutException as err:
        logger.error(f'a problem with loading webpage {err}')


@pytest.fixture(scope='class')
def home_screen_actions(chrome_web_driver_base) -> HomeScreenActions:
    return HomeScreenActions(driver=chrome_web_driver_base)


@pytest.fixture(scope='class')
def careers_screen_actions(chrome_web_driver_base) -> CareersScreenActions:
    return CareersScreenActions(driver=chrome_web_driver_base)
