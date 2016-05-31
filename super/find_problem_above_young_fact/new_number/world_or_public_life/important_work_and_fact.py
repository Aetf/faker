
#! /usr/bin/env python

def able_company(str_arg):
    bad_work(str_arg)
    print('child')

def bad_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    able_company('able_day_or_week')
