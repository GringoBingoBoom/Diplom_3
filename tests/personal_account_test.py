from data import Urls
import allure
from locators.login_page_locator import LoginPageLocator
from locators.profile_page import ProfilePageLocator
from pages.profile_page import ProfilePage

class TestPasswordRecovery:

    @allure.title('2.1 Личный кабинет. переход по клику на «Личный кабинет»')
    @allure.description('Личный кабинет. переход по клику на «Личный кабинет»')
    def test_personal_account_click_check_target_url(self, driver, payload, create_user):
        personal_page = ProfilePage(driver)
        personal_page.open_page(Urls.MAIN)
        personal_page.login_and_go_to_personal_account(payload)

        assert driver.current_url == Urls.PROFILE

    @allure.title('2.2 Личный кабинет. переход в раздел «История заказов»')
    @allure.description('Личный кабинет. переход в раздел «История заказов»')
    def test_personal_account_go_to_order_history(self, driver, payload, create_user):
        personal_page = ProfilePage(driver)
        personal_page.open_page(Urls.MAIN)
        personal_page.login_and_go_to_personal_account(payload)
        personal_page.wait_and_find_element(ProfilePageLocator.PROFILE_HISTORY_BUTTON).click()

        assert driver.current_url == Urls.ORDER_HISTORY

    @allure.title('2.3 Личный кабинет. Выход из аккаунта')
    @allure.description('Личный кабинет. Выход из аккаунта')
    def test_personal_account_logout(self, driver, payload, create_user):
        personal_page = ProfilePage(driver)
        personal_page.open_page(Urls.MAIN)
        personal_page.login_and_go_to_personal_account(payload)
        personal_page.wait_and_find_element(ProfilePageLocator.LOGOUT_BUTTON).click()
        personal_page.wait_and_find_element(LoginPageLocator.SIGN_IN_TITLE)

        assert driver.current_url == Urls.LOGIN
