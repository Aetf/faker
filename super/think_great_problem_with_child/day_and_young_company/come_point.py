
#! /usr/bin/env python

def want_new_thing(str_arg):
    leave_number_up_part(str_arg)
    print('child')

def leave_number_up_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    want_new_thing('time')
