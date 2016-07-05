
#! /usr/bin/env python

def little_company(str_arg):
    big_thing(str_arg)
    print('give_company')

def big_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_company('other_day')
