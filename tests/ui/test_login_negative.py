from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
import allure


def test_locked_out_user(login_page, page) -> None:
    login_page.navigate_to()
    login_page.expect_login_credentials_visible()
    login_page.type_username("locked_out_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()
    login_page.expect_error_message("Epic sadface: Sorry, this user has been locked out.")
    attach_screenshot(page, "Screenshot test_locked_out_user")


def test_user_name_or_password_is_incorrect(login_page, page) -> None:
    login_page.navigate_to()
    login_page.expect_login_credentials_visible()
    login_page.type_username("abcabc")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()
    login_page.expect_error_message("Epic sadface: Username and password do not match any user in this service")
    attach_screenshot(page, "Screenshot test_user_name_or_password_is_incorrect")

def test_user_name_and_password_are_missing(login_page, page) -> None:
    login_page.navigate_to()
    login_page.expect_login_credentials_visible()
    login_page.click_login_button()
    login_page.expect_error_message("Epic sadface: Username is required")
    attach_screenshot(page, "Screenshot test_user_name_and_password_are_missing")

def test_password_is_missing(login_page, page) -> None:
    login_page.navigate_to()
    login_page.expect_login_credentials_visible()
    login_page.type_username("abcabc")
    login_page.click_login_button()
    login_page.expect_error_message("Epic sadface: Password is required")
    attach_screenshot(page, "Screenshot test_password_is_missing")


def attach_screenshot(page, name):
    screenshot = page.screenshot()
    allure.attach(
        screenshot,
        name=name,
        attachment_type=allure.attachment_type.PNG,
    )
