
#! /usr/bin/env python

def bad_way_or_eye(str_arg):
    child(str_arg)
    print('time_and_bad_hand')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_way_or_eye('work')
