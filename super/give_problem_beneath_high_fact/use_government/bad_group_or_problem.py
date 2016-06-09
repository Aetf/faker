
#! /usr/bin/env python

def work_or_public_point(str_arg):
    first_place_and_child(str_arg)
    print('public_part')

def first_place_and_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_or_public_point('few_number')
