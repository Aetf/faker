
#! /usr/bin/env python

def man_and_bad_fact(str_arg):
    see_last_child(str_arg)
    print('old_fact')

def see_last_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man_and_bad_fact('new_work')
