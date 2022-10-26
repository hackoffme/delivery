import requests
from django.conf import settings
# telegram url

url = f"https://api.telegram.org/bot{settings.TOKEN}/"

def send_mess(text):
    params = {'chat_id': settings.CHANEL, 'text': text, 'parse_mode':'HTML'}
    # async with aiohttp.ClientSession() as session:
    #     async with session.post(url + 'sendMessage', data=params) as response:
    #         ret = await response.json()
    #         return ret
    response = requests.post(url + 'sendMessage', data=params)
    return response

# 0:00:00.408397 time фукнция асинхронна рекуест обычный
# 0:00:00.421930 time все обычно №1
# 0:00:00.403532 time и фукнция и рекуест асинхронны №2