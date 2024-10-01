from selenium.webdriver.common.by import By


class MainPageLocator:
    BUTTON_LOGIN_TO_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка 'Войти в аккаунт'
    MAIN_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    BUN = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    POP_UP_DETAILS = (By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]")
    ORDER_ID = (By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]//h2")
    ORDER_ID_CLOSE_BUTTON = (By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]//button")
    DETAILS_CLOSE_BUTTON = (By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]//button")
    INGREDIENT_COUNTERS = (By.XPATH, "//*[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']//*[contains(@class, 'counter_counter__num')]")
    DROP_ZONE = (By.XPATH, ".//*[@class='BurgerConstructor_basket__29Cd7 mt-25 ']")
    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")  # кнопка 'Личный Кабинет'
    BUTTON_CREATE_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']")
    POP_UP_INGREDIENT_DETAILS_CLOSE = (By.XPATH, ".//*[text()='Ваш заказ начали готовить']/../../../..")
    ORDER_ANIMATION = (By.XPATH, "//div[@class='Modal_modal__P3_V5']")
