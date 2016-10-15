
#! /usr/bin/env python

def think_number(str_arg):
    thing(str_arg)
    print('child')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    think_number('place')
