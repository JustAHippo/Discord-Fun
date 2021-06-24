import requests
import time
print("Type Bot Loaded Successfully!")
print(f"This bot makes it say you're typing 24/7")
aaa = input(f'Initiated. Press enter to continue(sometimes the console glitches out and does this anyways lol)')
channel_id = input(f'Channel ID(right click channel with dev mode on): ')
token = input(f'Discord Token(search how to grab): ')
URL = 'https://discord.com/api/v9/channels/' + channel_id + '/typing'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36', 
'authorization': token
}
print('Spam Started! Request 204 means successful!')
n = 5
while n < 696969:
    r = requests.post(URL, headers=headers)
    print(r)
    time.sleep(9)