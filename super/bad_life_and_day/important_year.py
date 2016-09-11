
#! /usr/bin/env python

def old_number(str_arg):
    early_child(str_arg)
    print('number_or_child')

def early_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    old_number('new_way')
