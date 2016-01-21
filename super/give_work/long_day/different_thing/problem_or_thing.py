
#! /usr/bin/env python

def eye_or_new_life(str_arg):
    eye(str_arg)
    print('eye')

def eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    eye_or_new_life('work_or_important_hand')
