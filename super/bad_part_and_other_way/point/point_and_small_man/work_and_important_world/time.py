
#! /usr/bin/env python

def leave_other_part_for_man(str_arg):
    thing(str_arg)
    print('say_problem')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    leave_other_part_for_man('new_way')
