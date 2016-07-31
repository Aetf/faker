
#! /usr/bin/env python

def thing(str_arg):
    child(str_arg)
    print('week')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('good_year_or_new_number')
