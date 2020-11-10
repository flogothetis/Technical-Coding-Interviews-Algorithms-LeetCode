from collections import deque

def createGraph (vertices, edges):
    adj_list = {i: [] for  i in range (vertices)}
    insToNode = {i: 0 for i in range(vertices)}
    for edge in edges:
        parent, child = edge[0], edge[1]
        adj_list[parent].append(child)
        insToNode[child] = insToNode.get(child,0) + 1
    return adj_list, insToNode

# Time Comp :O(V + E)
# Space: O(V+ E)
def topological_sort(vertices, edges):
    adj_list, insToNode = createGraph(vertices, edges)
    # Find source nodes
    source_nodes= []
    for node, count in insToNode.items():
        if ( count == 0):
            source_nodes.append(node)

    all_lists = []
    curr_list = []
    for ids in source_nodes:
            dfsUtil(ids, adj_list, curr_list, all_lists)

    return  all_lists


def dfsUtil (source, adj_list, curr_list, all_lists):
    curr_list.append(source)
    if (len(adj_list[source]) == 0):
        all_lists.append(curr_list.copy())
    for childen in adj_list[source]:
        dfsUtil(childen, adj_list, curr_list, all_lists)
    curr_list.pop()

def main():
  print("Task Orders: ")
  print(topological_sort(3, [[0, 1], [1, 2]]))

  print("Task Orders: ")
  print(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]]) )

  print("Task Orders: ")
  print(topological_sort(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]))


main()
