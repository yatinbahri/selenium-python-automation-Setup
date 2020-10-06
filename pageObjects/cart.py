from selenium import webdriver

class Cart:
    # Elements
    product_number_dropdown_xpath = "//option[contains(text(),'1x')]/ancestor::select"
    product_2x_xpath = "//option[contains(text(),'2x')]"
    checkout_button_xpath = "//ul[@class='checkout-types bottom']//button[@class='rma-button btn-proceed-checkout btn-checkout']"
    guest_radio_button_xpath = "//label[contains(text(),'Als Gast zur Kasse gehen')]"
    proceed_button_xpath = "//button[@id='onepage-guest-register-button']"

    def __init__(self, driver):
        self.driver = driver

    def increaseProductNumber(self):
        self.driver.find_element_by_xpath(self.product_number_dropdown_xpath).click()
        self.driver.find_element_by_xpath(self.product_2x_xpath).click()


    def proceedToCheckout(self):
        self.driver.find_element_by_xpath(self.checkout_button_xpath).click()

    def selectGuestRadio(self):
        self.driver.find_element_by_xpath(self.guest_radio_button_xpath).click()
        self.driver.find_element_by_xpath(self.proceed_button_xpath).click()