from selenium import webdriver
from data import Data, Urls, ApiUrls
import pytest
from api import ApiRequest
from helpers import CreatePayload


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def driver(request):
    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
    browser.maximize_window()

    yield browser

    browser.quit()


@pytest.fixture(scope='function')
def payload():
    return CreatePayload.create_payload()


@pytest.fixture(scope='function')
def create_user(payload):
    return ApiRequest.post(ApiUrls.CREATE_USER, payload)

