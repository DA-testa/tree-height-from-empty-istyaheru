# python3
# Ēriks Lijurovs, RDBD0 16. grupa, 221RDB041

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    visited = numpy.zeros((int(n)))
    steps_arr = numpy.zeros((int(n)))
    next = 0
    steps = 1

    for i in range(n-1):

        if parents[next] == -1:
            visited[i-1] = True
            steps_arr[i-1] = steps
            next = int(i)
            steps = 1
        elif visited[next] == True:
            visited[i-1] = True
            steps_arr[i-1] = steps_arr[next] + 1
            next = int(i)
            steps = 1
        else:
            visited[next] = True
            steps_arr[next] = int(steps)
            steps = steps + 1
            next = int(parents[next])
        
    for j in range(n-1):

        if max_height < int(steps_arr[int(j)]):
            max_height = int(steps_arr[int(j)])

    print(steps_arr[:])
    print(visited[:])

    return max_height


def main():
    # implement input form keyboard and from files
    choice = input()

    if choice.__contains__('F'):
        test = input()
        if test.__contains__('a'):
            return
        else:
            with open("test/" + test) as file:
                amount = int(file.readline())
                tree_str = file.readline().replace("\n", "").split(" ")
                tree = numpy.array(tree_str)
                print(tree)
                print(compute_height(amount, tree))
            file.close()
    elif choice.__contains__('I'):
        amount = int(input())
        tree_str = input().split(" ")
        tree = numpy.array(tree_str)
        print(tree)
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
#threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))