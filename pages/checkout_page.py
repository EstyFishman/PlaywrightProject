from playwright.sync_api import Page, expect
import allure


class CheckoutPage:
    def __init__(self, page: Page):
        self.__first_name = page.locator("[data-test=\"firstName\"]").describe("First name")
        self.__last_name = page.locator("[data-test=\"lastName\"]").describe("Last name")
        self.__postal_code = page.locator("[data-test=\"postalCode\"]").describe("Code")
        self.__massage_container = page.locator(".error-message-container").describe("Error")
        # self.__cancel=
        self.__continue = page.locator("[data-test=\"continue\"]").describe("Continue")
        self.__subtotal_label = page.locator("[data-test=\"subtotal-label\"]").describe("Subtotal label")
        self.__tax_label = page.locator("[data-test=\"tax-label\"]").describe("")
        self.__total_label = page.locator("[data-test=\"total-label\"]").describe("")
        self.__finish = page.locator("[data-test=\"finish\"]").describe("")

    def fill_details(self, f_name, l_name, code):
        with allure.step("Fill details"):
            self.__first_name.press_sequentially(f_name, delay=100)
            self.__last_name.press_sequentially(l_name, delay=100)
            self.__postal_code.fill(code)

    def continue_click(self):
        with allure.step("Continue"):
            self.__continue.click()

    def cancel(self):
        pass

    def finish(self):
        with allure.step("Finish"):
            self.__finish.click()
