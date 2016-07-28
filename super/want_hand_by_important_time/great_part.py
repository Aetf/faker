
#! /usr/bin/env python

def early_world(str_arg):
    number_or_small_case(str_arg)
    print('child')

def number_or_small_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_world('small_place_and_next_way')
