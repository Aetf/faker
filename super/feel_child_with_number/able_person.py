
#! /usr/bin/env python

def long_work(str_arg):
    big_thing(str_arg)
    print('new_government')

def big_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_work('bad_company')
