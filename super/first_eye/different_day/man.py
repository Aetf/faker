
#! /usr/bin/env python

def call_thing(str_arg):
    tell_child(str_arg)
    print('time')

def tell_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_thing('try_old_fact_about_old_part')
