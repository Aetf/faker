
#! /usr/bin/env python

def give_child(str_arg):
    small_place(str_arg)
    print('hand_or_child')

def small_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    give_child('use_time')
