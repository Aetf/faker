
#! /usr/bin/env python

def tell_man(str_arg):
    get_small_work(str_arg)
    print('man')

def get_small_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    tell_man('look_bad_day_at_time')
