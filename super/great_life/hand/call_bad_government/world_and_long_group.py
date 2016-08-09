
#! /usr/bin/env python

def go_child(str_arg):
    get_next_hand(str_arg)
    print('own_time')

def get_next_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    go_child('eye_and_work')
