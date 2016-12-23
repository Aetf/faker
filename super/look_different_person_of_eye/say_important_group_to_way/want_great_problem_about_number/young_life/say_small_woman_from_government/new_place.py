
#! /usr/bin/env python

def child(str_arg):
    early_problem(str_arg)
    print('early_man')

def early_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('know_problem_up_new_number')
