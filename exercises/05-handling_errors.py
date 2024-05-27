#!/usr/bin/env python3

def sum(a,b):
  try:
    sum = a + c
    return sum
  except Exception as e:
    error = e.args[0]
    print('''\n\nError:
        The Sum function had the following error: {}'''.format(error))

def subtract(a,b):
  try:
    subtract = a - b
    return subtract
  except Exception as e:
    error = e.args[0]
    print('''\n\nError:
        The Subtract function had the following error: {}'''.format(error))

if __name__ == '__main__':
    print("Sum: ", sum(6,8))
    print("Subtract: ", subtract(9,7))