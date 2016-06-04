
#! /usr/bin/env python

def feel_thing(str_arg):
    go_part(str_arg)
    print('leave_group')

def go_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    feel_thing('world_and_important_time')
