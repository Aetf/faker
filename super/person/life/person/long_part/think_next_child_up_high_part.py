
#! /usr/bin/env python

def own_fact(str_arg):
    case(str_arg)
    print('life')

def case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_fact('man')
