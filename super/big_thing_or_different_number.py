
#! /usr/bin/env python

def young_man(str_arg):
    woman(str_arg)
    print('part')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    young_man('last_case')
