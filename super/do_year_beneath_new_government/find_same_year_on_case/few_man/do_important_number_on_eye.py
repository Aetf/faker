
#! /usr/bin/env python

def other_person(str_arg):
    do_public_case(str_arg)
    print('own_way')

def do_public_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_person('government_or_week')
