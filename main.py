import requests
from requests import HTTPError


def print_resp(url):
    try:
        response = requests.get(url)

        # если ответ успешен, исключения задействованы не будут
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Если неверно указан URL адрес
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')


adress = 'https://api.github.com'
print('Посылаем запрос на' + adress)
print_resp(adress)
