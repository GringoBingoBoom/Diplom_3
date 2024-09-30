import pytest
from data import Urls, ApiUrls
import allure
from locators.base_page_locator import BasePageLocator
from locators.feed_page_locator import FeedPageLocator
from locators.main_page_locators import MainPageLocator
from locators.profile_page import ProfilePageLocator
from pages.main_page import MainPage
from api import ApiRequest
from helpers import CreatePayload


class TestOrderFeed:
    counter_dataset = [FeedPageLocator.COUNTER_ALL_TIME,
                       FeedPageLocator.COUNTER_TODAY]

    @allure.title('setup')
    def setup_method(self):
        self.teardown_payload = None

    @allure.title('4.1 Раздел «Лента заказов». если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.description('если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_on_order_with_popup_window_details(self, driver, payload, create_user):
        self.teardown_payload = payload

        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN)
        main_page.login(payload)

        main_page.drag_and_drop()

        main_page.wait_and_find_element(MainPageLocator.BUTTON_CREATE_ORDER).click()
        main_page.wait_presence(MainPageLocator.ORDER_ANIMATION)
        order_element = main_page.wait_and_find_element(MainPageLocator.ORDER_ID)
        order_id = order_element.text
        main_page.wait_element_clickable(MainPageLocator.ORDER_ID_CLOSE_BUTTON).click()
        main_page.wait_element_clickable(BasePageLocator.BUTTON_FEED).click()
        main_page.wait_and_find_element(FeedPageLocator.FEED_TITLE)
        locator = main_page.create_locator_by_text(FeedPageLocator.FEED_FIND_ORDER_TEMPLATE, order_id)
        main_page.wait_presence(locator).click()
        element = main_page.wait_and_find_element(MainPageLocator.POP_UP_DETAILS)

        assert 'opened' in element.get_attribute('class')

    @allure.title('4.2 Раздел «Лента заказов». заказы пользователя ')
    @allure.description('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_click_order_from_history_equal_order_fit(self, driver, payload, create_user):
        self.teardown_payload = payload

        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN)
        main_page.login(payload)

        main_page.drag_and_drop()

        main_page.wait_and_find_element(MainPageLocator.BUTTON_CREATE_ORDER).click()
        main_page.wait_presence(MainPageLocator.ORDER_ANIMATION)
        order_element = main_page.wait_and_find_element(MainPageLocator.ORDER_ID)
        order_id = order_element.text
        locator = main_page.create_locator_by_text(FeedPageLocator.FEED_FIND_ORDER_TEMPLATE, order_id)
        main_page.wait_element_clickable(MainPageLocator.ORDER_ID_CLOSE_BUTTON).click()

        main_page.login_and_go_to_personal_account()
        main_page.wait_presence(ProfilePageLocator.PROFILE_HISTORY_LIST)
        element_from_history = main_page.find_element(locator)
        order_id_from_history = element_from_history.text

        main_page.wait_element_clickable(BasePageLocator.BUTTON_FEED).click()
        main_page.wait_and_find_element(FeedPageLocator.FEED_TITLE)

        element_from_feed = main_page.find_element(locator)
        order_id_from_feed = element_from_feed.text

        assert order_id_from_history == f'#0{order_id}' and order_id_from_feed == f'#0{order_id}'

    @allure.title('4.3 Раздел «Лента заказов». Счетчики за все время и за день ')
    @allure.description('при создании нового заказа счётчики Выполнено за всё время и за день увеличиваются')
    @pytest.mark.parametrize('counter_locator', counter_dataset)
    def test_order_counter_all_time_increase_after_make_order(self, driver, counter_locator, payload, create_user):
        self.teardown_payload = payload

        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN)
        main_page.login(payload)

        main_page.wait_element_clickable(BasePageLocator.BUTTON_FEED).click()
        main_page.wait_and_find_element(FeedPageLocator.FEED_TITLE)

        counter_before = main_page.wait_and_find_element(counter_locator).text

        main_page.wait_element_clickable(BasePageLocator.BUTTON_CONSTRUCTOR).click()
        main_page.wait_and_find_element(MainPageLocator.MAIN_TITLE)

        main_page.drag_and_drop()

        main_page.wait_and_find_element(MainPageLocator.BUTTON_CREATE_ORDER).click()
        main_page.wait_presence(MainPageLocator.ORDER_ANIMATION)
        main_page.wait_element_clickable(MainPageLocator.ORDER_ID_CLOSE_BUTTON).click()

        main_page.wait_element_clickable(BasePageLocator.BUTTON_FEED).click()
        main_page.wait_and_find_element(FeedPageLocator.FEED_TITLE)

        counter_after = main_page.wait_and_find_element(counter_locator).text

        assert int(counter_before) + 1 == int(counter_after)

    @allure.title('4.4 Раздел «Лента заказов». после оформления заказа его номер появляется в разделе В работе.')
    @allure.description('после оформления заказа его номер появляется в разделе В работе.')
    def test_after_making_order_id_show_in_progress_section(self, driver, payload, create_user):
        self.teardown_payload = payload

        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN)
        main_page.login(payload)

        main_page.drag_and_drop()

        main_page.wait_and_find_element(MainPageLocator.BUTTON_CREATE_ORDER).click()
        main_page.wait_presence(MainPageLocator.ORDER_ANIMATION)

        order_element = main_page.wait_and_find_element(MainPageLocator.ORDER_ID)
        order_id = order_element.text
        locator = main_page.create_locator_by_text(FeedPageLocator.FEED_FIND_ORDER_STATUS_TEMPLATE, order_id)
        main_page.wait_element_clickable(MainPageLocator.ORDER_ID_CLOSE_BUTTON).click()

        main_page.wait_element_clickable(BasePageLocator.BUTTON_FEED).click()
        main_page.wait_and_find_element(FeedPageLocator.FEED_TITLE)

        element_from_feed = main_page.find_element(locator)

        assert element_from_feed.text == f'0{order_id}'

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
