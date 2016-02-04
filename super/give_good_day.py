
#! /usr/bin/env python

def work_good_problem(str_arg):
    hand(str_arg)
    print('tell_child')

def hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_good_problem('ask_world')
