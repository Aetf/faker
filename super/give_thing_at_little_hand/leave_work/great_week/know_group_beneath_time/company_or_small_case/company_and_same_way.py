
#! /usr/bin/env python

def use_different_man(str_arg):
    thing(str_arg)
    print('thing_and_part')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_different_man('first_group')
