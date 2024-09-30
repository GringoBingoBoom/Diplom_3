import allure
from locators.login_page_locator import LoginPageLocator
from locators.main_page_locators import MainPageLocator
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Ожидание локатора и клик по нему.')
    def wait_and_click_login_button(self):
        self.wait_and_click(MainPageLocator.BUTTON_LOGIN_TO_ACCOUNT)

    @allure.step('Вход в аккаунт')
    def login(self, payload):
        self.wait_and_find_element(MainPageLocator.MAIN_TITLE)
        self.wait_element_clickable(MainPageLocator.PERSONAL_ACCOUNT).click()
        self.wait_and_find_element(LoginPageLocator.EMAIL).send_keys(payload['email'])
        self.wait_and_find_element(LoginPageLocator.PASSWORD).send_keys(payload['password'])
        self.wait_element_clickable(LoginPageLocator.BUTTON_SIGNIN).click()
        self.wait_and_find_element(MainPageLocator.MAIN_TITLE)

    @allure.step('Заказ ингредиентов Drag and Drop')
    def drag_and_drop(self):
        action = self.action()
        source = self.wait_element_clickable(MainPageLocator.BUN)
        target = self.wait_element_clickable(MainPageLocator.DROP_ZONE)
        action.drag_and_drop(source, target).perform()
        action.release(source).perform()
