
#! /usr/bin/env python

def eye(str_arg):
    last_place(str_arg)
    print('other_child')

def last_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    eye('bad_number_and_group')
