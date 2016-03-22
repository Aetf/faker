
#! /usr/bin/env python

def use_thing(str_arg):
    part(str_arg)
    print('part')

def part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_thing('right_way')
