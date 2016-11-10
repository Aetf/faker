
#! /usr/bin/env python

def other_child_or_public_part(str_arg):
    old_work(str_arg)
    print('come_big_work_up_old_part')

def old_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_child_or_public_part('give_person')
