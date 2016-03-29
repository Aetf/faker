
#! /usr/bin/env python

def last_hand(str_arg):
    ask_world_to_child(str_arg)
    print('new_way_and_own_child')

def ask_world_to_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    last_hand('find_woman')
