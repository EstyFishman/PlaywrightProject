import allure


def test_e2e_1(login_page, inventory_page, cart_page, checkout_page):
    login_page.navigate_to()
    login_page.type_username("standard_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()
    login_page.expect_login_successful()
    inventory_page.add_jacket_to_cart()
    inventory_page.add_onesie_to_cart()
    inventory_page.go_to_cart()
    cart_page.remove_jacket()
    cart_page.continue_shopping()
    inventory_page.add_jacket_to_cart()
    inventory_page.go_to_cart()
    cart_page.checkout()
    checkout_page.fill_details("Esther", "Fishman", "123456")
    checkout_page.continue_click()
    checkout_page.finish()


def test_e2e_2(login_page, inventory_page, cart_page, checkout_page):
    login_page.navigate_to()
    login_page.type_username("standard_user")
    login_page.fill_password("secret_sauce")
    login_page.click_login_button()
    login_page.expect_login_successful()
    inventory_page.add_item("fleece-jacket")
    inventory_page.add_onesie_to_cart()
    inventory_page.go_to_cart()
    cart_page.checkout()
    checkout_page.fill_details("Annie", "Shay", "123456")
    checkout_page.continue_click()
    checkout_page.finish()
