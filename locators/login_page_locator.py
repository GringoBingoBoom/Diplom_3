from selenium.webdriver.common.by import By


class LoginPageLocator:
    BUTTON_RECOVERY_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")  # ссылка 'Восстановить пароль'
    SIGN_IN_TITLE = (By.XPATH, "//h2[text()='Вход']")  # заголовок страницы ВХОД
    EMAIL = (By.XPATH, "//*[text()='Email']/../input")
    PASSWORD = (By.XPATH, ".//*[text()='Пароль']/../input")
    BUTTON_SIGNIN = (By.XPATH, "//button[text()='Войти']")  # кнопка Войти
