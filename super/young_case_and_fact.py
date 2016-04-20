
#! /usr/bin/env python

def child(str_arg):
    say_long_time(str_arg)
    print('long_number')

def say_long_time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('young_hand')
