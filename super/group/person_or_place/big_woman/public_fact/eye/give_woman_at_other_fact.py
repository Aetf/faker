
#! /usr/bin/env python

def work_old_way(str_arg):
    point(str_arg)
    print('early_hand')

def point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_old_way('man')
