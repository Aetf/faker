
#! /usr/bin/env python

def child(str_arg):
    tell_other_number_of_first_work(str_arg)
    print('make_last_work_under_old_fact')

def tell_other_number_of_first_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('other_child')
