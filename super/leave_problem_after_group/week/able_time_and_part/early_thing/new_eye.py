
#! /usr/bin/env python

def child(str_arg):
    work_high_hand(str_arg)
    print('make_early_child')

def work_high_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('same_week')
