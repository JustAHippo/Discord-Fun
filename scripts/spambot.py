import requests
import time
print("Spam Bot Loaded Successfully!")
aaa = input(f'Initiated. Press enter to continue(sometimes the console glitches out and does this anyways lol)')
message = input("Message Spammed: ")
channel_id = input(f"Channel ID(use dev mode and left click the channel):")
token = input(f'Your Discord Token(search how to grab): ')
frequency = float(input(f"Frequency of spam(in seconds): "))
payload = {
    "content": message
}
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36', 
    "authorization": token
}
n = 5
print('Spam Started! Request 200 means successful!')
while n > 0:
    r = requests.post("https://discord.com/api/v9/channels/" + channel_id + "/messages", data=payload, headers=header)
    print(r)
    time.sleep(frequency)