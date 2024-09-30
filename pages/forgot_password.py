import allure
from data import Data
from locators.forgot_password_page_locator import ForgotPasswordPageLocator
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    @allure.step('Ожидание заголовка, поиск поля ввода почты, ввод почты, клик, ожидание нового локатора')
    def find_send_and_click_forgot_password(self):
        self.wait_and_find_element(ForgotPasswordPageLocator.TITLE)
        input_field = self.wait_and_find_element(ForgotPasswordPageLocator.INPUT_FIELD_EMAIL)
        input_field.send_keys(Data.EMAIL)
        self.wait_and_click(ForgotPasswordPageLocator.BUTTON_RECOVERY)
        self.wait_and_find_element(ForgotPasswordPageLocator.INPUT_FIELD_CODE)

    @allure.step('Ожидание и поиск кнопки показать-скрыть пароль, клик, возвращение значения класса на 3 уровня выше')
    def find_and_click_show_hide_password_button(self):
        self.wait_element_clickable(ForgotPasswordPageLocator.SHOW_HIDE_PASSWORD_BUTTON)
        element = self.wait_and_find_element(ForgotPasswordPageLocator.SHOW_HIDE_PASSWORD_BUTTON)
        element.click()
        return self.wait_and_find_element(ForgotPasswordPageLocator.PASSWORD_FIELD_STATE)

