
#! /usr/bin/env python

def case_and_work(str_arg):
    world(str_arg)
    print('early_time')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    case_and_work('week_and_year')
