# Time Complexity O(N + M)
def merge(intervals_a, intervals_b):
    result = []
    pointer_a = 0
    pointer_b = 0
    while (pointer_a < len(intervals_a) and pointer_b < len(intervals_b)):
        # Check conditions of overlapping
        a_overplaps_b = (intervals_b[pointer_b][0] <= intervals_a[pointer_a][0] <= intervals_b[pointer_b][1])

        b_overlaps_a = intervals_a[pointer_a][0] <= intervals_b[pointer_b][0] <= intervals_a[pointer_a][1]

        # Keep overlapped area
        if(a_overplaps_b or b_overlaps_a):
            result.append([max(intervals_a[pointer_a][0], intervals_b[pointer_b][0]),
                           min(intervals_a[pointer_a][1], intervals_b[pointer_b][1])])

        # Move forward the pointer finishing first
        if intervals_a[pointer_a][1] < intervals_b[pointer_b][1] and pointer_a < len(intervals_a) - 1:
            pointer_a += 1
        else:
            pointer_b += 1

    return result


def main():
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()
