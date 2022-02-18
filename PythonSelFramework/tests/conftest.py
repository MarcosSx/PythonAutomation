import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name', action='store', default='chrome'
    )


@pytest.fixture(scope='class')
def setup(request):
    global driver
    browser_name = request.config.getoption('browser_name')
    if browser_name in 'chrome':
        ser = Service('C:\\DEV\\Python\\drivers\\chromedriver.exe')
        op = webdriver.ChromeOptions()
        op.add_argument('--start-maximized')
        op.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(service=ser, options=op)
    elif browser_name in 'firefox':
        driver = webdriver.Firefox(executable_path='C:\\DEV\\Python\\drivers\\geckodriver.exe')
    elif browser_name in 'ie':
        print('IE driver')
    elif browser_name in 'opera':
        driver = webdriver.Firefox(executable_path='C:\\DEV\\Python\\drivers\\operadriver.exe')
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    driver.implicitly_wait(3)
    request.cls.driver = driver
    yield
    driver.close()
