import os
import config

def parse_words(text):
    with open(text, 'r') as text:
        line = text.readlines()[0]
        words = line.split()
    return words

def send_sms(num, msg):
    os.system(f'osascript send.scpt {config.NUM} "{msg}"')

if __name__ == "__main__":
    messages = parse_words('text.txt')
    for message in messages:
        send_sms(config.NUM, message)