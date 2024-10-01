from data import Urls
import allure
from pages.forgot_password import ForgotPasswordPage
from pages.login_page import LoginPage


class TestPasswordRecovery:

    @allure.title('1.1 Восстановление пароля. Переход на страницу')
    @allure.description('переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_recovery_page_check_target_url(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.LOGIN)
        login_page.wait_and_click_recovery_password()

        assert driver.current_url == Urls.FORGOT_PASSWORD

    @allure.title('1.2 Восстановление пароля. ввод почты и клик по кнопке «Восстановить»')
    @allure.description('ввод почты и клик по кнопке «Восстановить»')
    def test_input_email_click_password_recovery_button(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.open_page(Urls.FORGOT_PASSWORD)
        forgot_page.find_send_and_click_forgot_password()

        assert driver.current_url == Urls.RESET_PASSWORD

    @allure.title('1.3 Восстановление пароля. Клик по кнопке показать/скрыть пароль')
    @allure.description('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_click_on_show_hide_password_button(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.open_page(Urls.FORGOT_PASSWORD)
        forgot_page.find_send_and_click_forgot_password()
        element = forgot_page.find_and_click_show_hide_password_button()

        assert 'input_status_active' in element.get_attribute('class')
