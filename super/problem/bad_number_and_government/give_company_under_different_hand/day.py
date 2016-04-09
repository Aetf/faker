
#! /usr/bin/env python

def work_child(str_arg):
    look_good_work_with_large_case(str_arg)
    print('work_and_child')

def look_good_work_with_large_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_child('good_child')
