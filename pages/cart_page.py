from playwright.sync_api import Page, expect
import allure


class CartPage:
    def __init__(self, page: Page):
        self.__page = page
        self.__remove_jacket = page.locator("[data-test=\"remove-sauce-labs-fleece-jacket\"]").describe("")
        self.__continue_shopping = page.locator("[data-test=\"continue-shopping\"]").describe("")
        self.__checkout = page.locator("[data-test=\"checkout\"]").describe("")

    def remove_jacket(self):
        with allure.step("Removing jacket."):
            self.__remove_jacket.click()

    def continue_shopping(self):
        with allure.step("Continue shopping."):
            self.__continue_shopping.click()

    def checkout(self):
        with allure.step("Checkout"):
            self.__checkout.click()