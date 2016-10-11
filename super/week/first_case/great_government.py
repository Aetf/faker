
#! /usr/bin/env python

def other_child(str_arg):
    eye(str_arg)
    print('see_good_work')

def eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_child('leave_bad_thing_after_public_life')
