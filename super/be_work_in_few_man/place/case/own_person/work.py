
#! /usr/bin/env python

def say_long_man_in_case(str_arg):
    hand_and_little_work(str_arg)
    print('high_part')

def hand_and_little_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    say_long_man_in_case('own_part')
