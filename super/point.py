
#! /usr/bin/env python

def big_work_and_important_number(str_arg):
    say_last_fact(str_arg)
    print('small_fact')

def say_last_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_work_and_important_number('number_and_own_fact')
