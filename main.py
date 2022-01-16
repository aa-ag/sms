############------------ IMPORTS ------------############
import os
import config

############------------ GLOBAL VARIABLE(S) ------------############
recipient = config.NUM


############------------ FUNCTION(S) ------------############
def parse_words(text):
    with open(text, 'r') as text:
        line = text.readlines()[0]
        words = line.split()
    return words


def send_sms(num, msg):
    os.system(f'osascript send.scpt {recipient} "{msg}"')


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    messages = parse_words('text.txt')
    for message in messages:
        send_sms(recipient, message)
