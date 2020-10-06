from selenium import webdriver


class ProductSearch:
    # Elements
    add_to_cart_button_xpath = "//button[@id='addtocart-button-ajax']"
    cart_icon_xpath = "//p[contains(text(),'Warenkorb')]"

    def __init__(self, driver):
        self.driver = driver

    def addToCart(self):
        element = self.driver.find_element_by_xpath(self.add_to_cart_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def navigateToCart(self):
        element = self.driver.find_element_by_xpath(self.cart_icon_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()


