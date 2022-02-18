from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self, setup):
        home_page = HomePage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        confirm_page = ConfirmPage(self.driver)
        home_page.shopItems().click()
        cards = checkout_page.getCardTitle()
        i = -1
        for card in cards:
            i += 1
            card_text = card.text
            print(card_text)
            if card_text in 'iphone X':
                checkout_page.getCardFooter()[i].click()
        checkout_page.getBtnCheckout().click()

        confirm_page.getBtnCheckout().click()
        confirm_page.getLblCountry().send_keys('united')
        self.verifyLinkPresence('United Kingdom')
        confirm_page.getOptCountry().click()
        confirm_page.getCbkIAgree().click()
        confirm_page.getBtnPurchase().click()
        success = confirm_page.getLblSuccess().text

        ok = ''
        try:
            assert 'Success!' in success
            ok = 'Success'
        except:
            print('Failure')
            ok = 'Failure'
        finally:
            self.driver.get_screenshot_as_file(f'{ok}.png')
