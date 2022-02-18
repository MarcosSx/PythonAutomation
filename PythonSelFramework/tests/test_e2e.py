import pytest

from TestData.TestE2EData import TestE2EData
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self, setup, get_data):
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
            if card_text in get_data['product']:
                checkout_page.getCardFooter()[i].click()
        checkout_page.getBtnCheckout().click()

        confirm_page.getBtnCheckout().click()
        confirm_page.getLblCountry().send_keys(get_data['search'])
        self.verifyLinkPresence('country')
        confirm_page.getOptCountry().click()
        confirm_page.getCbkIAgree().click()
        confirm_page.getBtnPurchase().click()
        success = confirm_page.getLblSuccess().text

        # not defined yet screenschot method
        ok = ''
        try:
            assert get_data['success'] in success
            ok = get_data['success']
        except:
            print(get_data['failure'])
            ok = get_data['failure']
        finally:
            self.driver.get_screenshot_as_file(f'{ok}.png')

    @pytest.fixture(params=TestE2EData.test_e2e_data)
    def get_data(self, request):
        return request.param
