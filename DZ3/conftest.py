import pytest


# @pytest.fixture()
# def x_selector1():
#     return """/html/body/div/main/div/div/div[1]/form/div[1]/label/input"""
#
#
# @pytest.fixture()
# def x_selector2():
#     return """/html/body/div/main/div/div/div[1]/form/div[2]/label/input"""
#
#
# @pytest.fixture()
# def x_selector3():
#     return """//*[@id="app"]/main/div/div/div[2]/h2"""
#
#
# @pytest.fixture()
# def btn_selector():
#     return "button"


@pytest.fixture()
def create_post_btn():
    return '//*[@id="create-btn"]'


@pytest.fixture()
def input_title():
    return '//*[@id="create-item"]/div/div/div[1]/div/label/input'


@pytest.fixture()
def find_title():
    return '//*[@id="create-item"]/div/div/div[7]/div/button'

@pytest.fixture()
def find_post_name():
    return "/html/body/div[1]/main/div/div[1]/h1"

@pytest.fixture()
def find_contact_form():
    return '//*[@id="app"]/main/nav/ul/li[2]/a'


