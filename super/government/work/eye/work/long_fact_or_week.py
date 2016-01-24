
#! /usr/bin/env python

def great_day(str_arg):
    small_hand(str_arg)
    print('see_small_day')

def small_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    great_day('high_way')
