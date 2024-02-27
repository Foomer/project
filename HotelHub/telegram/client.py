import os

import requests


def send_message(text):
    # Получаем токен бота из переменных окружения
    token = os.environ.get("TELEGRAM_API_TOKEN")
    chat_id = "1186882770"




    # Отправляем POST-запрос к API Telegram для отправки сообщения
    response = requests.post(f"https://api.telegram.org/bot{token}/sendMessage".format(token=token),
                             data = {"chat_id": chat_id, "text": text})

    # Проверяем успешность запроса
    if response.status_code != 200:
        print("Ошибка при отправке сообщения в Telegram:", response.text)