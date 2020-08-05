import os
import config

def parse_words(file_path):
    with open(file_path, 'r') as f:
        line = f.readlines()[0]
        words = line.split()
    return words

def send_sms(num, msg):
    os.system(f'osascript send.scpt {config.NUM} "{msg}"')

if __name__ == "__main__":
    messages = parse_words('text.txt')
    for message in messages:
        send_sms(config.NUM, message)
