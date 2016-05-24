
#! /usr/bin/env python

def use_man(str_arg):
    woman(str_arg)
    print('world')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_man('group')
