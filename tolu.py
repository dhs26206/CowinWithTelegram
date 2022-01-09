import os
api_key = os.environ['api']
user_id = os.environ['user']

import requests

def telegram_bot_sendtext(bot_message):

   send_text = 'https://api.telegram.org/bot' + api_key + '/sendMessage?chat_id=' + user_id + '&parse_mode=Markdown&text=' + bot_message

   response=requests.get(send_text)
   print(response)


