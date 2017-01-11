
#! /usr/bin/env python

def call_early_company_in_child(str_arg):
    take_number(str_arg)
    print('want_next_life')

def take_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_early_company_in_child('week')
