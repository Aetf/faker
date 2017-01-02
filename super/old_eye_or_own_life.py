
#! /usr/bin/env python

def try_own_place(str_arg):
    use_next_person(str_arg)
    print('work')

def use_next_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    try_own_place('hand')
