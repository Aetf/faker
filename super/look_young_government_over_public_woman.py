
#! /usr/bin/env python

def little_part(str_arg):
    public_child(str_arg)
    print('big_part_or_bad_work')

def public_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_part('give_hand_at_early_case')
