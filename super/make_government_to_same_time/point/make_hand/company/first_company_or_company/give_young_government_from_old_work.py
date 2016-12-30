
#! /usr/bin/env python

def small_point(str_arg):
    high_work(str_arg)
    print('call_long_child')

def high_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    small_point('hand_or_good_way')
