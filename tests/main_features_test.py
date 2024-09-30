from data import Urls, ApiUrls
import allure
from locators.base_page_locator import BasePageLocator
from locators.feed_page_locator import FeedPageLocator
from locators.main_page_locators import MainPageLocator
from pages.main_page import MainPage
from api import ApiRequest
from helpers import CreatePayload


class TestMainFeatures:

    @allure.title('setup')
    def setup_method(self):
        self.teardown_payload = None

    @allure.title('3.1 Проверка основного функционала. Переход по клику на «Конструктор»')
    @allure.description('Проверка основного функционала. Переход по клику на «Конструктор»')
    def test_redirect_by_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.FEED)
        main_page.wait_and_find_element(FeedPageLocator.FEED_TITLE)
        main_page.wait_and_find_element(BasePageLocator.BUTTON_CONSTRUCTOR).click()

        assert driver.current_url == Urls.MAIN

    @allure.title('3.2 Проверка основного функционала. переход по клику на «Лента заказов»')
    @allure.description('Проверка основного функционала. переход по клику на «Лента заказов»')
    def test_redirect_by_feed_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN)
        main_page.wait_and_find_element(MainPageLocator.MAIN_TITLE)
        main_page.wait_and_find_element(BasePageLocator.BUTTON_FEED).click()

        assert driver.current_url == Urls.FEED

    @allure.title('3.3 Проверка основного функционала. Кликнуть на ингредиент')
    @allure.description('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient_popup_details(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN)
        main_page.wait_and_find_element(MainPageLocator.MAIN_TITLE)
        main_page.wait_and_find_element(MainPageLocator.BUN).click()
        element = main_page.wait_and_find_element(MainPageLocator.POP_UP_DETAILS)

        assert 'Modal_modal_opened' in element.get_attribute('class')

    @allure.title('3.4 Проверка основного функционала. всплывающее окно закрывается кликом по крестику')
    @allure.description('всплывающее окно закрывается кликом по крестику')
    def test_popup_details_close_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN)
        main_page.wait_and_find_element(MainPageLocator.MAIN_TITLE)
        main_page.wait_and_find_element(MainPageLocator.BUN).click()
        main_page.wait_and_find_element(MainPageLocator.POP_UP_DETAILS)
        main_page.wait_and_find_element(MainPageLocator.DETAILS_CLOSE_BUTTON).click()
        element = main_page.find_element(MainPageLocator.POP_UP_INGREDIENT_DETAILS_CLOSE)

        assert 'opened' not in element.get_attribute('class')

    @allure.title('3.5 Проверка основного функционала. добавление ингредиента')
    @allure.description('при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_add_ingredient_check_increase_counter(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN)
        main_page.wait_and_find_element(MainPageLocator.MAIN_TITLE)
        main_page.drag_and_drop()
        element = main_page.wait_and_find_element(MainPageLocator.INGREDIENT_COUNTERS)

        assert element.text == '2'

    @allure.title('3.6 Проверка основного функционала. залогиненный пользователь может оформить заказ')
    @allure.description('залогиненный пользователь может оформить заказ')
    def test_registered_user_can_place_order(self, driver, payload, create_user):
        self.teardown_payload = payload
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN)
        main_page.login(payload)
        main_page.drag_and_drop()
        main_page.wait_and_find_element(MainPageLocator.BUTTON_CREATE_ORDER).click()
        element = main_page.wait_and_find_element(MainPageLocator.POP_UP_DETAILS)

        assert 'opened' in element.get_attribute('class')

    @allure.title('teardown')
    def teardown_method(self, payload_login):
        """
        удаляем данные на основании payload. Через авторизацию получаем токен
        """
        if self.teardown_payload:
            payload_login = CreatePayload.payload_for_login(self.teardown_payload)
            response = ApiRequest.post(ApiUrls.AUTHORIZATION, payload_login)
            if response.status_code == 200:  # если пользователь существует удаляем данные о нем
                r = response.json()
                payload_token = CreatePayload.payload_authorization(r['accessToken'])
                response_del = ApiRequest.delete(ApiUrls.USER_INFO, payload_token)
                print(response_del.json(), self.teardown_payload)
                assert response_del.status_code == 202, f'Значение {response_del.status_code=} не равно 202'