import allure
from pages.base_page import BasePage


class FeedPage(BasePage):

    @allure.step('Создание локатора по id заказа')
    def create_locator_by_text(self, template, text):
        return (template[0], template[1].substitute(text=text))
