
#! /usr/bin/env python

def work_or_thing(str_arg):
    person(str_arg)
    print('case')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_or_thing('do_work_beneath_case')
