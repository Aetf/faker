
#! /usr/bin/env python

def go_work(str_arg):
    company_or_fact(str_arg)
    print('case')

def company_or_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    go_work('child')
