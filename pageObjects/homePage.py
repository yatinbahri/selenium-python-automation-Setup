from selenium import webdriver


class HomePage:
    # Home Page elements
    search_bar_xpath = "//input[@id='search']"
    select_product_xpath = "//li[@class='selected']//a"

    def __init__(self, driver):
        self.driver = driver

    def searchForProduct(self, product):
        self.driver.find_element_by_xpath(self.search_bar_xpath).clear()
        self.driver.find_element_by_xpath(self.search_bar_xpath).send_keys(product)

    def selectProduct(self):
        self.driver.find_element_by_xpath(self.select_product_xpath).click()
