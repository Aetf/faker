
#! /usr/bin/env python

def thing(str_arg):
    work_part(str_arg)
    print('work_and_early_work')

def work_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('problem_or_high_place')
