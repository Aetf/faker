
#! /usr/bin/env python

def eye(str_arg):
    person(str_arg)
    print('early_eye')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    eye('work_and_thing')
