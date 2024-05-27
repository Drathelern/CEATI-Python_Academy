#!/usr/bin/env python3

def err_handling_decorator(func):
    '''
    This decorator is to set error handling to all the methods in which it is required and to indicate which was the specific error.
    '''
    def error_handling(*args):
        try:
            return func(*args)
        except Exception as e:
            error        = e.args[0]
            func_name    = func.__name__
            print('''\n\nError:
                The {} function had the following error: {}'''.format(func_name, error))

    return error_handling


@err_handling_decorator
def sum(a,b):
  sum = a + c

  return sum

@err_handling_decorator
def subtract(a,b):
  subtract = a - b

  return subtract

if __name__ == '__main__':
    print("Sum: ", sum(6,8))
    print("Subtract: ", subtract(9,7))