
#! /usr/bin/env python

def see_group_with_public_case(str_arg):
    right_work(str_arg)
    print('call_part_after_thing')

def right_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    see_group_with_public_case('other_man')
