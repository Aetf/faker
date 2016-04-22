
#! /usr/bin/env python

def bad_eye(str_arg):
    work_and_first_child(str_arg)
    print('point_and_work')

def work_and_first_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_eye('great_thing')
