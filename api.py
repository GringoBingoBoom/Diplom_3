import allure
import requests
from data import ApiUrls


class ApiRequest:
    # метод запроса POST возвращает список из логина, пароля, кода ответа и текст
    @staticmethod
    @allure.step('API запрос POST по BASE_URL+api_url')
    def post(api_url: str, payload: dict):
        # отправляем запрос post
        return requests.post(ApiUrls.BASE_URL + api_url, json=payload)

    @staticmethod
    @allure.step('API запрос GET по BASE_URL+api_url')
    def get(api_url: str, payload: dict = None):
        # отправляем запрос get
        if payload:
            return requests.get(ApiUrls.BASE_URL + api_url, json=payload)
        else:
            return requests.get(ApiUrls.BASE_URL + api_url)

    @staticmethod
    @allure.step('API запрос DELETE по BASE_URL+api_url')
    def delete(api_url: str, payload_token: dict):
        # отправляем запрос delete
        return requests.delete(ApiUrls.BASE_URL + api_url, headers=payload_token)

