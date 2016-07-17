
#! /usr/bin/env python

def say_big_problem(str_arg):
    work_and_other_child(str_arg)
    print('other_life')

def work_and_other_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    say_big_problem('part')
