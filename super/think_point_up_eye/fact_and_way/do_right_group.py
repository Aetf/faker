
#! /usr/bin/env python

def large_child(str_arg):
    leave_person_with_fact(str_arg)
    print('world')

def leave_person_with_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    large_child('big_week_and_important_man')
