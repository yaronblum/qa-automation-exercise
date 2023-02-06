from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions

from typing import List
from infra.logger import logger
from data.careers import Careers as CareersData
from data.common import Common
from time import sleep


class CareersScreen:

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver

    def find_and_tap_RD_sections(self):
        logger.info("searching for R&D button")
        self.driver.find_element(By.XPATH, value=CareersData.r_and_d_button).click()

    def iter_over_positions(self):
        """
        listing all available positions, then iter over each one and perform test logic
        """
        current_positions: List = [
            element.text for element in self.driver.find_elements(by=By.CLASS_NAME, value=CareersData.careers_selections_class_name)
        ]

        if not len(current_positions):
            raise AssertionError('No Positions Found')

        logger.info(f"found positions: {current_positions}")

        for position in current_positions:
            self.driver.find_element(By.XPATH, value=CareersData.generic_position_button.format(position)).click()
            self.apply_to_position()
            self.driver.back()

    def apply_to_position(self):
        sleep(3) # "handling iFrame wait-conditions was a bit tricky, instead we are waiting statically"
        self.driver.switch_to.frame('grnhse_iframe')
        WebDriverWait(self.driver, timeout=10).until(expected_conditions.element_to_be_clickable(
            self.driver.find_element(By.ID, 'first_name'))
        )
        self.submit_first_name()
        self.submit_last_name()
        self.submit_phone_number()
        self.submit_email()
        self.submit_linked_in()

    def submit_first_name(self):
        self.driver.find_element(by=By.ID, value="first_name").send_keys(Common.first_name)

    def submit_last_name(self):
        self.driver.find_element(by=By.ID, value='last_name').send_keys(Common.last_name)

    def submit_phone_number(self):
        self.driver.find_element(by=By.ID, value='phone').send_keys(Common.phone)

    def submit_email(self):
        self.driver.find_element(by=By.ID, value='email').send_keys(Common.email)

    def submit_linked_in(self):
        self.driver.find_element(by=By.ID, value="job_application_answers_attributes_0_text_value").send_keys(Common.linkedin)
