from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    btnCheckout = (By.XPATH, '//*[@class="btn btn-success"]')
    lblCountry = (By.ID, 'country')
    options = (By.XPATH, '//a[contains(text(),"United Kingdom")]')
    optCountry = (By.LINK_TEXT, 'United Kingdom')
    cbkIAgree = (By.XPATH, '//label[@for="checkbox2"]')
    btnPurchase = (By.CSS_SELECTOR, 'input[type="submit"]')
    lblSuccess = (By.TAG_NAME, 'strong')

    def getBtnCheckout(self):
        return self.driver.find_element(*ConfirmPage.btnCheckout)

    def getLblCountry(self):
        return self.driver.find_element(*ConfirmPage.lblCountry)

    def getOptions(self):
        return self.driver.find_element(*ConfirmPage.options)

    def getOptCountry(self):
        return self.driver.find_element(*ConfirmPage.optCountry)

    def getCbkIAgree(self):
        return self.driver.find_element(*ConfirmPage.cbkIAgree)

    def getBtnPurchase(self):
        return self.driver.find_element(*ConfirmPage.btnPurchase)

    def getLblSuccess(self):
        return self.driver.find_element(*ConfirmPage.lblSuccess)

