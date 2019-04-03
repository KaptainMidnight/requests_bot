import requests
from time import sleep


class API:
    __token = "<token>"
    __url = f"https://api.telegram.org/bot{__token}/"

    def __init__(self):
        self.get_updates()

    def get_updates(self):
        response = requests.get(self.__url + 'getUpdates')
        return response.json()

    def last_update(self, data):
        results = data['result']
        total_updates = len(results) - 1
        return results[total_updates]

    def get_chat_id(self, update):
        chat_id = update['message']['chat']['id']
        return chat_id

    def send_mess(self, chat, text):
        params = {'chat_id': chat, 'text': text}
        response = requests.post(self.__url + 'sendMessage', data=params)
        return response


def main():
    bot = API()
    update_id = bot.last_update(bot.get_updates())['update_id']
    while True:
        if update_id == bot.last_update(bot.get_updates())['update_id']:
            bot.send_mess(bot.get_chat_id(bot.last_update(bot.get_updates())), 'test')
            update_id += 1


if __name__ == '__main__':
    main()
