
#! /usr/bin/env python

def use_man(str_arg):
    do_great_man_in_case(str_arg)
    print('small_case')

def do_great_man_in_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_man('small_child_and_world')
