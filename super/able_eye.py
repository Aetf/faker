
#! /usr/bin/env python

def see_last_place(str_arg):
    point_and_child(str_arg)
    print('leave_good_way_to_child')

def point_and_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    see_last_place('hand_or_high_group')
