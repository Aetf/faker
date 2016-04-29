
#! /usr/bin/env python

def ask_early_child_in_place(str_arg):
    leave_little_life_at_thing(str_arg)
    print('early_hand')

def leave_little_life_at_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    ask_early_child_in_place('week_or_little_problem')
