
#! /usr/bin/env python

def use_good_man(str_arg):
    different_child(str_arg)
    print('place')

def different_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_good_man('first_number')
