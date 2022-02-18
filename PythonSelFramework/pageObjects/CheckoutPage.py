from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, '.card-title a')
    cardFooter = (By.CSS_SELECTOR, '.card-footer button')
    btnCheckout = (By.XPATH, '//a[contains(text(),"Checkout")]')

    def getCardTitle(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def getBtnCheckout(self):
        return self.driver.find_element(*CheckoutPage.btnCheckout)
