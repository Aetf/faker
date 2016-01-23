
#! /usr/bin/env python

def ask_small_problem(str_arg):
    ask_new_work_on_new_world(str_arg)
    print('public_work')

def ask_new_work_on_new_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    ask_small_problem('person')
