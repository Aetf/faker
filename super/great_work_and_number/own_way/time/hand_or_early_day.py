
#! /usr/bin/env python

def case(str_arg):
    call_world_with_time(str_arg)
    print('work_point_with_new_child')

def call_world_with_time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    case('long_week')
