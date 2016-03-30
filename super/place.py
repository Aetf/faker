
#! /usr/bin/env python

def old_man(str_arg):
    good_man(str_arg)
    print('be_right_man')

def good_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    old_man('early_work')
