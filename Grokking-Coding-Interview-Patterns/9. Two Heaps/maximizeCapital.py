'''
Problem Statement #

Given a set of investment projects with their respective profits, we need to find the most profitable projects. We
are given an initial capital and are allowed to invest only in a fixed number of projects. Our goal is to choose
projects that give us the maximum profit. Write a function that returns the maximum total capital after selecting
the most profitable projects. We can start an investment project only when we have the required capital. Once a project
is selected, we can assume that its profit has become our capital.
'''

from heapq import *

# Time Complexity : O(NlogN  + KlongN)
# Space Complexity O(N)
def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    min_heap = []
    max_heap = []
    current_capital = initialCapital
    # push all capitals into a min heap
    for i in range(len(capital)): # NlogN
        heappush(min_heap, [capital[i], i])

    for _ in range (numberOfProjects): # KlogN
        # find the projects that can be bought with current_capital
        while ( min_heap and min_heap[0][0] <= current_capital):
            capital, i = heappop(min_heap)
            heappush(max_heap, -profits[i])
        if max_heap:
            current_capital+= -heappop(max_heap)
        else:
            break

    return current_capital


def main():
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()
