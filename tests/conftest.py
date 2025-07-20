import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)


@pytest.fixture
def inventory_page(page: Page):
    return InventoryPage(page)


@pytest.fixture
def cart_page(page: Page):
    return CartPage(page)


@pytest.fixture
def checkout_page(page: Page):
    return CheckoutPage(page)


@pytest.fixture
def login_page_with_login(page: Page):
    lp = LoginPage(page)
    lp.navigate()
    return lp
