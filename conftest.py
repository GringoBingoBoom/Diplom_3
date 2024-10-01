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
    user = ApiRequest.post(ApiUrls.CREATE_USER, payload)

    yield user

    # teardown
    payload_login = CreatePayload.payload_for_login(payload)
    response = ApiRequest.post(ApiUrls.AUTHORIZATION, payload_login)
    if response.status_code == 200:  # если пользователь существует удаляем данные о нем
        r = response.json()
        payload_token = CreatePayload.payload_authorization(r['accessToken'])
        response_del = ApiRequest.delete(ApiUrls.USER_INFO, payload_token)
        print(response_del.json(), payload)
        assert response_del.status_code == 202, f'Значение {response_del.status_code=} не равно 202'

