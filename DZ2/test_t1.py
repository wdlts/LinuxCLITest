import time

import yaml

from module import Site

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])


# def test_step1(x_selector1, x_selector2, x_selector3, btn_selector, error_code):
#
#     input1 = site.find_element("xpath", x_selector1)
#     input1.send_keys(testdata["login"])
#
#     input2 = site.find_element("xpath", x_selector2)
#     input2.send_keys(testdata["password"])
#
#     btn = site.find_element("css", btn_selector)
#     btn.click()
#     err_label = site.find_element("xpath", x_selector3).text
#
#     time.sleep(5)
#     site.driver.close()
#
#     assert err_label == error_code, "test_step1 FAIL"


def test_step2(x_selector1, x_selector2, x_selector3, btn_selector, create_post_btn, input_title, find_title, find_post_name):
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys(testdata["login"])

    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys(testdata["password"])

    btn = site.find_element("css", btn_selector)
    btn.click()
    time.sleep(2)
    create_post_btn = site.find_element("xpath", create_post_btn)
    create_post_btn.click()
    time.sleep(2)
    input3 = site.find_element("xpath", input_title)
    input3.send_keys("RANDOMNAME")

    btn2 = site.find_element("xpath", find_title)
    btn2.click()
    time.sleep(5)
    find_post_name = site.find_element("xpath", find_post_name)
    assert find_post_name.text == "RANDOMNAME", "test_step1 FAIL"
    site.driver.close()
