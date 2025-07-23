from playwright.sync_api import Page, expect
import allure


class InventoryPage:
    def __init__(self, page: Page):
        self.__page = page
        self.__add_jacket = page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").describe(
            "Add to cart")
        self.__add_onesie = page.locator("[data-test=\"add-to-cart-sauce-labs-onesie\"]").describe("Add to cart")
        self.__go_to_cart = page.locator("[data-test=\"shopping-cart-link\"]").describe("Go to cart")

    def add_jacket_to_cart(self):
        with allure.step("Adding the jacket to the cart."):
            print(self.__add_jacket.is_visible())
            print(self.__add_jacket.is_enabled())  # True?
            self.__add_jacket.click()

    def add_onesie_to_cart(self):
        with allure.step("Adding the onesie to the cart."):
            self.__add_onesie.click()

    def go_to_cart(self):
        with allure.step("Going to the cart."):
            self.__go_to_cart.click()

    def add_item(self, item_name):
        with allure.step(f"Adding {item_name} to the cart."):
            add_button = self.__page.locator(f"[data-test='add-to-cart-sauce-labs-{item_name}']").describe(
                f"Add {item_name} to cart")
            expect(add_button).to_be_visible()
            expect(add_button).to_be_enabled()
            add_button.click()