
#! /usr/bin/env python

def child(str_arg):
    number(str_arg)
    print('ask_next_case')

def number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('call_right_hand_after_company')
