from selenium.webdriver.common.by import By
from string import Template


class FeedPageLocator:
    FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    COUNTER_ALL_TIME = (By.XPATH, "//*[text()='Выполнено за все время:']/..//p[contains(@class, 'Order')]")
    COUNTER_TODAY = (By.XPATH, "//*[text()='Выполнено за сегодня:']/..//p[contains(@class, 'Order')]")
    FEED_FIND_ORDER_TEMPLATE = (By.XPATH, Template(".//*[text()='#0$text']"))
    FEED_FIND_ORDER_STATUS_TEMPLATE = (By.XPATH, Template("//*[text()='В работе:']/..//*[text()='$text']"))
