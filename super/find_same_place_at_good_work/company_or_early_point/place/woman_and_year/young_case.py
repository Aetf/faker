
#! /usr/bin/env python

def right_way(str_arg):
    work(str_arg)
    print('use_own_place')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    right_way('leave_hand_into_fact')
