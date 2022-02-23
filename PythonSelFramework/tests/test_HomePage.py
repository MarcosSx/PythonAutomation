import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, get_data):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        home_page.getLblName().send_keys(get_data['firstName'])
        log.info(f'Name filled in the form: [{get_data["firstName"]}]')
        home_page.getLblEmail().send_keys(get_data['email'])
        log.info(f'Email filled in the form: [{get_data["email"]}]')
        home_page.getCheckbox().click()
        self.selectOptionByText(home_page.getSelect(), get_data['gender'])
        home_page.getBtnSubmit().click()
        alert_text = home_page.getAlert().text
        assert 'Success!' in alert_text
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePageData)
    def get_data(self, request):
        return request.param
