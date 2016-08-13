
#! /usr/bin/env python

def use_few_time(str_arg):
    place(str_arg)
    print('place')

def place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_few_time('other_woman')
