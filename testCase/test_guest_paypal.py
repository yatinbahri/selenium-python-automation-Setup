from pageObjects.homePage import HomePage
from pageObjects.productSearch import ProductSearch
from pageObjects.cart import Cart
import time
import pytest


class Test_001_Guest_Paypal():
    baseURL = "https://www.roastmarket.de/"
    product = "Alps Coffee Crème Schümli"

    def test_website_checker(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        title = self.driver.title

        if title == "Kaffee und Espresso online kaufen im Shop von roastmarket.":
            self.driver.save_screenshot(".//screenshots//" + "Pass_homePageTitle.png")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".//screenshots//"+"Fail_homePageTitle.png")
            self.driver.close()
            assert False

    def test_search_product(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        home = HomePage(self.driver)
        home.searchForProduct(self.product)
        home.selectProduct()
        time.sleep(2)

        # validation
        if self.driver.find_element_by_xpath("//h1[contains(text(),'Alps Coffee Crème Schümli')]"):
            self.driver.save_screenshot(".//screenshots//" + "Pass_Product_search.png")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".//screenshots//" + "Fail_Product_search.png")
            self.driver.close()
            assert False


    def test_add_product_to_cart(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        home = HomePage(self.driver)
        home.searchForProduct(self.product)
        home.selectProduct()
        time.sleep(2)

        pro = ProductSearch(self.driver)
        pro.addToCart()
        pro.navigateToCart()


    def test_proceed_to_checkout(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        home = HomePage(self.driver)
        home.searchForProduct(self.product)
        home.selectProduct()
        time.sleep(2)

        pro = ProductSearch(self.driver)
        pro.addToCart()
        pro.navigateToCart()


        cart = Cart(self.driver)
        cart.increaseProductNumber()
        time.sleep(2)
        cart.proceedToCheckout()
        time.sleep(2)
        cart.selectGuestRadio()
        self.driver.close()




