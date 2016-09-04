
#! /usr/bin/env python

def child(str_arg):
    big_company(str_arg)
    print('try_life')

def big_company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('other_time')
