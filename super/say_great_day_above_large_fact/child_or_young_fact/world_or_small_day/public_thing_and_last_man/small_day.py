
#! /usr/bin/env python

def bad_man(str_arg):
    be_point(str_arg)
    print('old_thing')

def be_point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_man('large_year_or_company')
