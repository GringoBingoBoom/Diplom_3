from selenium.webdriver.common.by import By


class ForgotPasswordPageLocator:
    INPUT_FIELD_EMAIL = (By.XPATH, "//label[text()='Email']/../input")  # поле ввода восстановления пароля
    TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")   # заголовок
    BUTTON_RECOVERY = (By.XPATH, "//button[text()='Восстановить']")  # кнопка Выход из личного кабинета
    INPUT_FIELD_CODE = (By.XPATH, "//label[text()='Введите код из письма']")
    SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH, "//div[@class='input__container']//*[name()='path']")
    PASSWORD_FIELD_STATE = (By.XPATH, "//div[@class='input__container']//*[name()='path']/../../..")
