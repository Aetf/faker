
#! /usr/bin/env python

def bad_way_and_big_work(str_arg):
    go_next_hand(str_arg)
    print('say_same_world_in_world')

def go_next_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_way_and_big_work('small_number')
