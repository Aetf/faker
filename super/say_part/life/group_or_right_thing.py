
#! /usr/bin/env python

def person(str_arg):
    call_bad_thing(str_arg)
    print('day')

def call_bad_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person('few_work')
