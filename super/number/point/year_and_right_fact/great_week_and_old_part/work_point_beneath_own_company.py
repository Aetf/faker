
#! /usr/bin/env python

def thing(str_arg):
    work(str_arg)
    print('thing_or_problem')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('want_first_world')
