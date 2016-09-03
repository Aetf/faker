
#! /usr/bin/env python

def think_last_thing(str_arg):
    man(str_arg)
    print('other_eye')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    think_last_thing('great_work')
