
#! /usr/bin/env python

def time(str_arg):
    hand(str_arg)
    print('long_work')

def hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    time('thing')
