from .locators import TestProductPagesLocators
from .base_page import BasePage

class TestProductPages(BasePage):
    def should_be_add_product(self):
        login_link = self.browser.find_element(*TestProductPagesLocators.ADD_PRODUCT)
        login_link.click()

    def should_be_message_add(self):
        product_name = self.browser.find_element(*TestProductPagesLocators.PRODUCT_NAME).text
        message_name = self.browser.find_element(*TestProductPagesLocators.MESSAGE_ADD).text
        assert product_name in message_name, "product name not true"

    def should_be_message_basket_price(self):
        message_basket_total = self.browser.find_element(*TestProductPagesLocators.MESSAGE_BASKET).text
        product_price = self.browser.find_element(*TestProductPagesLocators.PRODUCT_PRICE).text
        assert product_price in message_basket_total, "Total price not true"