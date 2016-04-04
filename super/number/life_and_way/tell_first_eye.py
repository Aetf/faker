
#! /usr/bin/env python

def eye_and_man(str_arg):
    work_child(str_arg)
    print('hand')

def work_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    eye_and_man('long_thing')
