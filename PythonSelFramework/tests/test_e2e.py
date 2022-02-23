import pytest

from TestData.TestE2EData import TestE2EData
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self, setup, get_data):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        confirm_page = ConfirmPage(self.driver)
        home_page.shopItems().click()
        log.info('getting all the card titles')
        cards = checkout_page.getCardTitle()
        i = -1
        for card in cards:
            i += 1
            card_text = card.text
            log.info(card_text)
            if card_text in get_data['product']:
                checkout_page.getCardFooter()[i].click()
        checkout_page.getBtnCheckout().click()

        confirm_page.getBtnCheckout().click()
        confirm_page.getLblCountry().send_keys(get_data['search'])
        self.verifyLinkPresence(get_data['country'])
        log.info('Entering the country name as united')
        confirm_page.getOptCountry().click()
        confirm_page.getCbkIAgree().click()
        confirm_page.getBtnPurchase().click()
        success = confirm_page.getLblSuccess().text
        log.info(f'Text received from application is [{success}]')
        assert "Successs" in success

    @pytest.fixture(params=TestE2EData.test_e2e_data)
    def get_data(self, request):
        return request.param
