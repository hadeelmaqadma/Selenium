import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def setup():
    # if browser == 'chrome':
    #     driver = webdriver.Chrome(service=Service('C:\webdrivers\chromedriver.exe'))
    #     print("Launching Chrome browser")
    # elif browser == 'firefox':
    #     driver = webdriver.firefox(service=Service('C:\webdrivers\geckodriver.exe'))
    #     print("Launching firefox browser")
    driver = webdriver.Chrome(service=Service('C:\webdrivers\chromedriver.exe'))
    return driver


def pytest_addoption(parser):  # get the value from the cli --browser chrome or --browser firefox
    parser.addoption("--browser")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

#  *********** Creating HTML Reports ***********#
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'customer'
    config._metadata['Tester'] = 'Hadeel'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    # can add more data
    metadata.pop("Plugins", None)
