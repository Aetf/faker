
#! /usr/bin/env python

def say_number(str_arg):
    child(str_arg)
    print('number')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    say_number('new_group')
