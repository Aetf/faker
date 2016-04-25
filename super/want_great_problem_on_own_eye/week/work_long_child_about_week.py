
#! /usr/bin/env python

def child(str_arg):
    man_or_new_problem(str_arg)
    print('last_thing')

def man_or_new_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('world')
