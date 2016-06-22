
#! /usr/bin/env python

def thing(str_arg):
    child(str_arg)
    print('company_or_person')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('place')
