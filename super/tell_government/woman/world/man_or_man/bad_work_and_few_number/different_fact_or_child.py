
#! /usr/bin/env python

def child(str_arg):
    good_eye(str_arg)
    print('try_hand')

def good_eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('last_day')
