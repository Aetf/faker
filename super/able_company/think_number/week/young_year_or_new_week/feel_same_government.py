
#! /usr/bin/env python

def big_problem(str_arg):
    leave_person_in_little_world(str_arg)
    print('large_part')

def leave_person_in_little_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_problem('leave_thing')
