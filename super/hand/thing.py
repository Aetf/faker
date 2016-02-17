
#! /usr/bin/env python

def child(str_arg):
    world(str_arg)
    print('ask_eye')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('work_high_part')
