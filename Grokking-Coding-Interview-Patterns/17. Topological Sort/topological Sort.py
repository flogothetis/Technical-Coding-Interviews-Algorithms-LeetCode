from collections import deque

def createGraph (vertices, edges):
    adj_list = {i: [] for  i in range (vertices)}

    for edge in edges:
        parent, child = edge[0], edge[1]
        adj_list[parent].append(child)
    return adj_list

# Time Comp :O(V + E)
# Space: O(V+ E)
def topological_sort(vertices, edges):
    visited = [False] * vertices
    adj_list = createGraph(vertices, edges)
    q = deque ()
    for i in range(vertices):
        if (visited[i] == False):
            dfsUtil(i, adj_list, visited, q)

    # Position of elements in q
    pos = [0] *vertices
    for i in range(vertices):
        pos[q[i]] = i

    # Detect Cycle:
    for i in range (vertices):
        for edge in adj_list[i]:
            if pos[i] > pos[edge]:
                return []

    return list (q)


def dfsUtil (source, adj_list, visited, q):
    visited[source] = True
    for  childen in adj_list[source]:
       if ( visited[childen] == False):
        dfsUtil(childen, adj_list, visited,q)
    q.appendleft(source)

def main():
  print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1], [1,2]])))
  print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))
main ()