
#! /usr/bin/env python

def long_work(str_arg):
    child(str_arg)
    print('call_right_number_with_hand')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_work('use_eye')
