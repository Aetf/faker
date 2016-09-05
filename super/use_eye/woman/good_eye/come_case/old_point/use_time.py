
#! /usr/bin/env python

def little_man(str_arg):
    company_or_work(str_arg)
    print('first_man')

def company_or_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_man('eye')
