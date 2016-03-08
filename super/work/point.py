
#! /usr/bin/env python

def call_early_life(str_arg):
    eye_or_next_eye(str_arg)
    print('problem')

def eye_or_next_eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_early_life('call_right_person')
