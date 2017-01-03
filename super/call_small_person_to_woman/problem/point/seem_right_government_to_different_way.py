
#! /usr/bin/env python

def child(str_arg):
    make_last_company_for_child(str_arg)
    print('eye')

def make_last_company_for_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('company')
