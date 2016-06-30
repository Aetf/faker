
#! /usr/bin/env python

def man_or_person(str_arg):
    say_different_time_at_point(str_arg)
    print('new_time')

def say_different_time_at_point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man_or_person('big_company')
