from selenium.webdriver.common.by import By


class ProfilePageLocator:
    PROFILE_HISTORY_BUTTON = (By.XPATH, ".//a[text()='История заказов']")
    PROFILE_TITLE = (By.XPATH, ".//*[text()='В этом разделе вы можете изменить свои персональные данные']")
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
    PROFILE_HISTORY_LIST = (By.XPATH, "//div[contains(@class,'OrderHistory')]")

