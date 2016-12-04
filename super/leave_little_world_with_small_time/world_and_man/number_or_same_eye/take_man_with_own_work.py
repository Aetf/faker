
#! /usr/bin/env python

def work_child_after_place(str_arg):
    work_and_good_thing(str_arg)
    print('see_high_number')

def work_and_good_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_child_after_place('new_life_and_number')
