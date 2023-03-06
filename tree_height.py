# python3
# Ēriks Lijurovs, RDBD0 16. grupa, 221RDB041

import sys
import threading
import numpy
import os


def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    steps_arr = numpy.zeros([n])

    for element in range(int(n)):
        
        if parents[element] == -1:
            steps = 1
        else:
            steps = int(element_steps(element, parents, steps_arr) + 1)

        if max_height < steps:
            max_height = steps

    return max_height

def element_steps(element, parents, steps_arr):

    if parents[element] != -1:
        steps_arr[element] = element_steps(parents[element], parents, steps_arr) + 1

    return steps_arr[element]


def main():
    # implement input form keyboard and from files
    choice = input()

    if choice.__contains__('F'):
        test = input()
        
        if test.__contains__('a'):
            return
        else:
            gh_bypass = os.path.join(os.getcwd(), 'test', test)
            with open(gh_bypass) as file:
                amount = int(file.readline())
                tree_str = list(map(int, file.readline().split(" ")))
                tree = numpy.array(tree_str)
                print(compute_height(amount, tree))
                
            file.close()
    elif choice.__contains__('I'):
        amount = int(input())
        tree_str = list(map(int, input().split(" ")))
        tree = numpy.array(tree_str)
        print(compute_height(amount, tree))
    else:
        print("Please enter I or F!")
        return

    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))