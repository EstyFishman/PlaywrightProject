import allure


def test_standard_user(login_page, page) -> None:
    login_page.navigate_to()
    login_page.expect_login_credentials_visible()
    login_page.type_username("standard_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()
    login_page.expect_login_successful()


def test_standard_user_with_enter(login_page, page) -> None:
    login_page.navigate_to()
    login_page.expect_login_credentials_visible()
    login_page.type_username("standard_user")
    login_page.fill_password("secret_sauce")
    page.keyboard.press("Enter")
    login_page.expect_login_successful()


def test_performance_glitch_user(login_page, page) -> None:
    login_page.navigate_to()
    login_page.expect_login_credentials_visible()
    login_page.type_username("performance_glitch_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()
    login_page.expect_login_successful()


def test_visual_user(login_page, page) -> None:
    login_page.navigate_to()
    login_page.expect_login_credentials_visible()
    login_page.type_username("visual_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()
    login_page.expect_login_successful()


def attach_screenshot(page, name):
    screenshot = page.screenshot()
    allure.attach(
        screenshot,
        name=name,
        attachment_type=allure.attachment_type.PNG,
    )
