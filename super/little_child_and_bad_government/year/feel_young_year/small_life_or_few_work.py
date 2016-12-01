
#! /usr/bin/env python

def use_case(str_arg):
    little_way(str_arg)
    print('work')

def little_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_case('different_eye')
