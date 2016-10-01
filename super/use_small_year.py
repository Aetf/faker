
#! /usr/bin/env python

def work_and_place(str_arg):
    look_eye(str_arg)
    print('other_eye')

def look_eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_and_place('work')
