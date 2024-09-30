import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocator
from locators.profile_page import ProfilePageLocator


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание видимости элемента')
    def wait_and_find_element(self, locator) -> WebElement:
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))

    @allure.step('Открытие страницы')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Ожидание что по элементу можно кликнуть и клик')
    def wait_and_click(self, locator):
        self.wait_element_clickable(locator).click()

    @allure.step('Ожидание что по элементу можно кликнуть')
    def wait_element_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))
        return WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable(locator))

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def action(self):
        return ActionChains(self.driver)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидание видимости элемента')
    def wait_invisibility(self, locator) -> WebElement:
        return WebDriverWait(self.driver, 10).until(ec.invisibility_of_element(locator))

    @allure.step('Переход в личную страницу')
    def login_and_go_to_personal_account(self):
        self.wait_element_clickable(MainPageLocator.PERSONAL_ACCOUNT).click()
        self.wait_and_find_element(ProfilePageLocator.PROFILE_TITLE)
        self.wait_and_find_element(ProfilePageLocator.PROFILE_HISTORY_BUTTON).click()

    @allure.step('Ожидание наличия элемента на странице')
    def wait_presence(self, locator) -> WebElement:
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))

    @allure.step('Создание локатора по тексту')
    def create_locator_by_text(self, template, text):
        return (template[0], template[1].substitute(text=text))


