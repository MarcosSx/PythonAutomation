from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, 'Shop')
    lblName = (By.CSS_SELECTOR, '[name="name"]')
    lblEmail = (By.NAME, 'email')
    checkBox = (By.ID, 'exampleCheck1')
    select = (By.ID, 'exampleFormControlSelect1')
    alert = (By.CSS_SELECTOR, '[class*="alert-success"]')
    btnSubmit = (By.XPATH, '//input[@value="Submit"]')

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)

    def getLblName(self):
        return self.driver.find_element(*HomePage.lblName)

    def getLblEmail(self):
        return self.driver.find_element(*HomePage.lblEmail)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkBox)

    def getSelect(self):
        return self.driver.find_element(*HomePage.select)

    def getAlert(self):
        return self.driver.find_element(*HomePage.alert)

    def getBtnSubmit(self):
        return self.driver.find_element(*HomePage.btnSubmit)
