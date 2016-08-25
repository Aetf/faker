
#! /usr/bin/env python

def child(str_arg):
    last_time(str_arg)
    print('eye')

def last_time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('day')
