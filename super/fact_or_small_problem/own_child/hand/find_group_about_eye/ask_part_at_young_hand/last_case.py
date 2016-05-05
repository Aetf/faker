
#! /usr/bin/env python

def work_number_on_thing(str_arg):
    go_long_hand(str_arg)
    print('thing')

def go_long_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_number_on_thing('eye')
