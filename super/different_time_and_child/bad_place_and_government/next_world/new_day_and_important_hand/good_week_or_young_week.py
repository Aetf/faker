
#! /usr/bin/env python

def child(str_arg):
    world(str_arg)
    print('able_thing')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('call_work_for_few_eye')
