#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        ch = '\0'
    else:
        ch = sentence[0]

    return (len(sentence), ch)
