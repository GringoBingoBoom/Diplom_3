import allure
from locators.login_page_locator import LoginPageLocator
from locators.main_page_locators import MainPageLocator
from locators.profile_page import ProfilePageLocator
from pages.base_page import BasePage


class ProfilePage(BasePage):
    @allure.step('Переход в личную страницу')
    def login_and_go_to_personal_account(self, payload):
        self.wait_and_find_element(MainPageLocator.MAIN_TITLE)
        self.wait_element_clickable(MainPageLocator.PERSONAL_ACCOUNT).click()
        self.wait_and_find_element(LoginPageLocator.EMAIL).send_keys(payload['email'])
        self.wait_and_find_element(LoginPageLocator.PASSWORD).send_keys(payload['password'])
        self.wait_element_clickable(LoginPageLocator.BUTTON_SIGNIN).click()
        self.wait_and_find_element(MainPageLocator.MAIN_TITLE)
        self.wait_element_clickable(MainPageLocator.PERSONAL_ACCOUNT).click()
        self.wait_and_find_element(ProfilePageLocator.PROFILE_TITLE)