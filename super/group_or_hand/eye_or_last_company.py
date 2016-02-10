
#! /usr/bin/env python

def other_company(str_arg):
    work(str_arg)
    print('place')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_company('large_place_or_long_thing')
