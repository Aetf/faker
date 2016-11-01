
#! /usr/bin/env python

def man_and_eye(str_arg):
    good_hand(str_arg)
    print('other_group')

def good_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man_and_eye('leave_thing')
