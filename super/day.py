
#! /usr/bin/env python

def world(str_arg):
    hand(str_arg)
    print('other_work')

def hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world('get_last_group_to_large_case')
