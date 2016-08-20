
#! /usr/bin/env python

def work_small_world_in_child(str_arg):
    life_or_small_eye(str_arg)
    print('other_part')

def life_or_small_eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_small_world_in_child('feel_day')
