
#! /usr/bin/env python

def thing(str_arg):
    tell_few_child(str_arg)
    print('next_thing_and_other_man')

def tell_few_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('eye')
