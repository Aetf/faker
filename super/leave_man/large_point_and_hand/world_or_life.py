
#! /usr/bin/env python

def work_or_company(str_arg):
    long_world(str_arg)
    print('work')

def long_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_or_company('great_number')
