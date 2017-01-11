
#! /usr/bin/env python

def bad_company(str_arg):
    group_or_work(str_arg)
    print('own_person')

def group_or_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_company('child')
