from selenium.webdriver.common.by import By


class BasePageLocator:
    BUTTON_FEED = (By.XPATH, "//p[text()='Лента Заказов']")
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")

