
#! /usr/bin/env python

def bad_company(str_arg):
    thing(str_arg)
    print('new_child')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_company('able_day')
