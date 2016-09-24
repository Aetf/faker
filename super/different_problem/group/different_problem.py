
#! /usr/bin/env python

def person(str_arg):
    want_bad_group_with_high_case(str_arg)
    print('last_group')

def want_bad_group_with_high_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person('last_group')
