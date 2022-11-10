import requests
from django.conf import settings
from django.http import HttpResponseServerError
import logging

logger = logging.getLogger(__name__)

url = f"https://api.telegram.org/bot{settings.TOKEN}/"

def send_mess(text):
    params = {'chat_id': settings.CHANEL, 'text': text, 'parse_mode':'HTML'}
    response = requests.post(url + 'sendMessage', data=params)
    if response.status_code != 200:
        logger.info(response.status_code)
        logger.info(text)
        logger.info(response.text)
        raise HttpResponseServerError
    
    return response
