from playwright.sync_api import Page, expect
import allure


class InventoryPage:
    def __init__(self, page: Page):
        self.__page = page
        self.__add_jacket = page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").describe(
            "Add to cart jacket")
        self.__add_onesie = page.locator("[data-test=\"add-to-cart-sauce-labs-onesie\"]").describe("Add to cart")
        self.__go_to_cart = page.locator("[data-test=\"shopping-cart-link\"]").describe("Go to cart")

    def add_jacket_to_cart(self):
        with allure.step("Adding the jacket to the cart."):
            self.__add_jacket()