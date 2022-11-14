import requests
from django.conf import settings
from django.http import HttpResponseServerError
import logging

logger = logging.getLogger(__name__)

url = f"https://api.telegram.org/bot{settings.TOKEN}/"


def split_text(text: str, l=4000):
    if len(text) <= l:
        return [text]
    ret = []
    text = text.split('\n')
    message = ''
    for item in text:
        if len(message)+len(item) >= l:
            ret.append(message)
            message = ''
        message += f'{item}\n'
    message and ret.append(message)
    return ret


def send_mess(text: str):
    params = {'chat_id': settings.CHANEL, 'text': text, 'parse_mode': 'HTML'}
    response = requests.post(url + 'sendMessage', data=params)
    for item in split_text(text):
        if response.status_code != 200:
            logger.info(response.status_code)
            logger.info(item)
            logger.info(response.text)
            raise HttpResponseServerError
