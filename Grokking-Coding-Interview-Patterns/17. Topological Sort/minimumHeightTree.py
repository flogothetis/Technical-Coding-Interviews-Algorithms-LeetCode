from collections import  deque


#  Time Comp : O(V+E)
# Space Comp: O(V)
def minimumHeightTree (vertices, edgees):
    # Find key idea ....
    # Intermediate Nodes will give the best result..
    # Solution -> Remove all the leaf nodes until having one or two intermediates

    inDegree = {i: 0 for i in range (vertices)}
    adj_list = {i:[] for i in range (vertices)}

    for parent, child in edgees :
        adj_list[parent].append(child)
        adj_list[child].append (parent)
        inDegree[parent] = inDegree[parent] + 1
        inDegree[child] += 1


    leaves = deque()
    # Find leaves
    for i in range (vertices):
        if (inDegree[i] == 1 ):
            leaves.append(i)

    totalElements  = vertices
    while (totalElements > 2):
        totalElements -= len(leaves)
        for i in range (len(leaves)):
            node = leaves.popleft()

            for child in adj_list[node]:
                inDegree[child]-=1
                if (inDegree[child] == 1):
                    leaves.append(child)

    return list(leaves)

def main():
  print("Roots of MHTs: " +
        str(minimumHeightTree(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
  print("Roots of MHTs: " +
        str(minimumHeightTree(4, [[0, 1], [0, 2], [2, 3]])))
  print("Roots of MHTs: " +
        str(minimumHeightTree(4, [[1, 2], [1, 3]])))


main()