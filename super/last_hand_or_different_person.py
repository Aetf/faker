
#! /usr/bin/env python

def work_or_different_place(str_arg):
    public_world_and_long_man(str_arg)
    print('other_hand')

def public_world_and_long_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_or_different_place('say_problem')
