import allure
from locators.login_page_locator import LoginPageLocator
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Ожидание локатора заголовка страницы, поиск кнопки воссьтановления пароля и клик.')
    def wait_and_click_recovery_password(self):
        self.wait_and_find_element(LoginPageLocator.SIGN_IN_TITLE)
        self.wait_and_click(LoginPageLocator.BUTTON_RECOVERY_PASSWORD)

