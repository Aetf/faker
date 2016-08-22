
#! /usr/bin/env python

def fact(str_arg):
    early_world(str_arg)
    print('old_number')

def early_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    fact('number_and_group')
