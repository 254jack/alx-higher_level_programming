#!/usr/bin/python3
if __name__ == '__main__':

    def magic_calculation(a, b):

        from calculator_1 import add, sub
        if a < b:
            sum = add(a, b)
            for i in range(4, 6):
                sum = add(sum, i)
            return sum
        else:
            return sub(a, b)
