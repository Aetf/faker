
#! /usr/bin/env python

def world(str_arg):
    person(str_arg)
    print('child')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world('bad_case_and_group')
