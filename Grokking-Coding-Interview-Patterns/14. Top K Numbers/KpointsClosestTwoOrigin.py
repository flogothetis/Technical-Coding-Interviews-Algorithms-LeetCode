'''
Problem Statement #

Given an array of points in the a 2D2D2D plane, find ‘K’ closest points to the origin.
'''




from heapq import *

# Time Comp : O(NlogK)
# Space Comp : O(K)
class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __lt__(self, other):
    self.euclidean_dist() > other.euclidean_dist()

  def print_point(self):
    print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

  def euclidean_dist (self):
      return (self.x ** 2 + self.y **2) ** (1/2)

def find_closest_points(points, k):
  result = []
  max_heap = []

  for i in range(k):
      heappush(max_heap, points[i])

  for  i in range ( k, len(points)):
      if (points[i].euclidean_dist() < max_heap[0].euclidean_dist()):
          heappop(max_heap)
          heappush(max_heap, points[i])

  return  list(max_heap)


def main():

  result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
  print("Here are the k points closest the origin: ", end='')
  for point in result:
    point.print_point()


main()


