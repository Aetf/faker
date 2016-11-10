
#! /usr/bin/env python

def few_eye_and_big_thing(str_arg):
    eye(str_arg)
    print('few_part')

def eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    few_eye_and_big_thing('bad_point')
