
#! /usr/bin/env python

def child(str_arg):
    government(str_arg)
    print('time')

def government(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('see_time_beneath_work')
