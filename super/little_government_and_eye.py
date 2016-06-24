
#! /usr/bin/env python

def child_and_number(str_arg):
    bad_person(str_arg)
    print('eye')

def bad_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_and_number('child')
