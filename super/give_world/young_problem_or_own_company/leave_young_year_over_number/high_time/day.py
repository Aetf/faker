
#! /usr/bin/env python

def great_life(str_arg):
    little_part(str_arg)
    print('new_life')

def little_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    great_life('try_part_under_high_way')
