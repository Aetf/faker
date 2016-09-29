
#! /usr/bin/env python

def good_company(str_arg):
    woman(str_arg)
    print('last_time')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_company('woman')
