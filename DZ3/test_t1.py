import time
from testpage import OperationsHelper
from conftest2 import browser
import module
import logging


# def test_step1(browser):
#     logging.info("Test1 start")
#     testpage = OperationsHelper(browser)
#     testpage.go_to_site()
#     testpage.enter_login("test")
#     testpage.enter_pass("test")
#     testpage.click_login_button()
#
#     assert testpage.get_error_text() == "401"

def test_step2(browser):
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(module.login)
    testpage.enter_pass(module.password)
    testpage.click_login_button()
    time.sleep(4)
    testpage.click_contact_form()
    time.sleep(4)
    assert testpage.check_contact_form() == "Contact us!"

    testpage.enter_data_in_contact_form()

    assert testpage.check_name_field_input() == "TESTDATA"
    assert testpage.check_email_field_input() == "TESTDATA@TESTDATA.com"
    assert testpage.check_content_field_input() == "TESTTESTTEST"

    testpage.click_contact_us_button()
    time.sleep(2)
    assert testpage.get_alert_text() == "Form successfully submitted"
    time.sleep(5)
