import time
import logging

from selenium.webdriver.common.by import By

from BaseApp import BasePage


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """/html/body/div/main/div/div/div[1]/form/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """/html/body/div/main/div/div/div[1]/form/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_CONTACT_FORM = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_CONTACT_US = (By.XPATH, """//*[@id="app"]/main/div/div/h1""")
    LOCATOR_YOUR_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_YOUR_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTENT_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BUTTON = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Login button click")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
        text = error_field.text
        logging.info(f'Text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD}')
        return text

    def click_contact_form(self):
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_FORM).click()

    def check_contact_form(self):
        contact_us = self.find_element(TestSearchLocators.LOCATOR_CONTACT_US, time=2).text
        return contact_us

    def enter_data_in_contact_form(self):
        your_name_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_NAME_FIELD)
        your_name_field.clear()
        your_name_field.send_keys("TESTDATA")

        your_email_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_EMAIL_FIELD)
        your_email_field.clear()
        your_email_field.send_keys("TESTDATA@TESTDATA.com")

        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FIELD)
        content_field.clear()
        content_field.send_keys("TESTTESTTEST")

    def check_name_field_input(self):
        input_text = self.find_element(TestSearchLocators.LOCATOR_YOUR_NAME_FIELD, time=2)
        return input_text.get_attribute("value")

    def check_email_field_input(self):
        input_text = self.find_element(TestSearchLocators.LOCATOR_YOUR_EMAIL_FIELD, time=2)
        return input_text.get_attribute("value")

    def check_content_field_input(self):
        input_text = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FIELD, time=2)
        return input_text.get_attribute("value")

    def click_contact_us_button(self):
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BUTTON).click()

    def alert_get_text(self):
        time.sleep(2)
        logging.info("Get alert message")
        alert_message = self.get_alert_text()
        logging.info(f"Alert message - {alert_message}")
        return alert_message


