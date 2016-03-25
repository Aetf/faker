
#! /usr/bin/env python

def other_child(str_arg):
    use_company(str_arg)
    print('go_big_work')

def use_company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_child('high_life')
