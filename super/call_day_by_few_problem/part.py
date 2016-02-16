
#! /usr/bin/env python

def look_life_at_next_world(str_arg):
    child(str_arg)
    print('child')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    look_life_at_next_world('give_child_in_woman')
