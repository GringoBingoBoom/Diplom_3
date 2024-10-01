class Urls:
    MAIN = "https://stellarburgers.nomoreparties.site/"
    LOGIN = f"{MAIN}login"
    PROFILE = f"{MAIN}profile"
    FORGOT_PASSWORD = f"{MAIN}forgot-password"
    RESET_PASSWORD = f"{MAIN}reset-password"
    FEED = f"{MAIN}feed"
    ORDER_HISTORY = f"{MAIN}order-history"


FAKE_CEED = 2128506  # ceed для faker


class Data:
    EMAIL = "sergeyvelichko12222@yandex.ru"


class ApiUrls:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api"
    CREATE_USER = "/auth/register"
    AUTHORIZATION = "/auth/login"
    USER_INFO = "/auth/user"
