#!/usr/bin/env python3
import readline
import operator

op = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
    '^': operator.pow
}

def calculate(arg):
    # stack for calculator
    tokens = arg.split()
    stack = []
    
    # process tokens
    for token in tokens:
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            val2 = int(stack.pop())
            val1 = int(stack.pop())

            # look up function in table
            func = op[token]
            result = func(val1, val2)

            stack.append(result)

    return int(stack[0])

def main():
    while True:
        result = calculate(input('rpn calc> '))
        print(result)

if __name__ == '__main__':
    main()
