
#! /usr/bin/env python

def other_company(str_arg):
    look_big_child_by_group(str_arg)
    print('group')

def look_big_child_by_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_company('leave_case_in_place')
