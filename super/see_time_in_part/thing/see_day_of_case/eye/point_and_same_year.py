
#! /usr/bin/env python

def different_company(str_arg):
    thing(str_arg)
    print('thing')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_company('small_time')
