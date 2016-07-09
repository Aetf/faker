
#! /usr/bin/env python

def other_child(str_arg):
    use_different_group_from_point(str_arg)
    print('tell_company')

def use_different_group_from_point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_child('place')
