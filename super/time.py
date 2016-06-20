
#! /usr/bin/env python

def man(str_arg):
    know_bad_child(str_arg)
    print('number')

def know_bad_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('first_number')
