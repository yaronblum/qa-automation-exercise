from data.scripts import Commands
from selenium.webdriver.common.by import By
from data.home_screen import HomeScreen as HomeScreenData


class HomeScreen:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_bottom_of_web_page(self):
        self.driver.execute_script(Commands.scroll_to_bottom)

    def tap_on_careers_footer(self):
        self.driver.find_element(by=By.XPATH, value=HomeScreenData.careers_button_reg_ex).click()

