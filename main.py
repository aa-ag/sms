############------------ IMPORTS ------------############
import os
import config

############------------ GLOBAL VARIABLE(S) ------------############
recipient = config.NUM


############------------ FUNCTION(S) ------------############
def parse_words(text):
    '''
     opens text file and returns a list of words
    '''
    text = open(text, 'r')
    line = text.readlines()[0]
    return line


def send_sms(num, msg):
    '''
     execytes scpt script which sends a msg to a recipient
    '''
    os.system(f'osascript send.scpt {recipient} "{msg}"')


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    messages = parse_words('text.txt')
    send_sms(recipient, messages)
