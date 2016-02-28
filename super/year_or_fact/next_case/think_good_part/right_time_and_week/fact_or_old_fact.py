
#! /usr/bin/env python

def see_child(str_arg):
    company(str_arg)
    print('company_and_fact')

def company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    see_child('think_week')
