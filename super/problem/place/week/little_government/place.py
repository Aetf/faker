
#! /usr/bin/env python

def good_case(str_arg):
    work_or_part(str_arg)
    print('part')

def work_or_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_case('part_and_work')
