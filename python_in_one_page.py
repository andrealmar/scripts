#Python in One Page
#author: andrealmar

import os


def main():
    print('Hello World!')
    print("This is Alice!!")
    print("This is Bob\'s greeting.")

    foo(5, 10)

    print ('=' * 10)
    text = 'The current working directory is '
    print(text + os.getcwd())

    fruits = ['apples', 'oranges', 'bananas']

    for fruit in fruits:
        print('I like to eat ', fruit)

    print('Çount to ten:' )
    for i in range(1, 11):
        print(i)


def foo(a, b):
    value = a + b

    print('%s plus %s is equal to %s' % (a, b, value))

    if value < 50:
        print('foo')
    elif (value >= 50) and ((a == 42) or (b == 24)):
        print('bar')
    else:
        print('moo')

    ''' A multi-
            line string, but can also be a multi-line comment.'''

    return value # This is a one-line comment

if __name__ == '__main__':
    main()