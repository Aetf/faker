
#! /usr/bin/env python

def person(str_arg):
    man(str_arg)
    print('early_world')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person('world')
