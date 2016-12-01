
#! /usr/bin/env python

def child(str_arg):
    problem(str_arg)
    print('call_same_week')

def problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('last_hand')
