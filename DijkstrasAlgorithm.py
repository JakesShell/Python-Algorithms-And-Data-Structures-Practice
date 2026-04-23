"""
Dijkstra's Algorithm

Given an adjacency list and a starting vertex, return the shortest
distance from the start to each vertex. Unreachable vertices are -1.

Time: O(V^2 + E)
Space: O(V)
"""

def dijkstrasAlgorithm(start, edges):
    numberOfVertices = len(edges)
    minDistancesFromStart = [float("inf")] * numberOfVertices
    minDistancesFromStart[start] = 0
    visited = set()

    while len(visited) < numberOfVertices:
        currentVertex, currentDistance = getNextClosestUnvisitedVertex(
            minDistancesFromStart, visited
        )

        if currentDistance == float("inf"):
            break

        visited.add(currentVertex)

        for neighborVertex, weight in edges[currentVertex]:
            if neighborVertex in visited:
                continue

            newDistance = currentDistance + weight
            if newDistance < minDistancesFromStart[neighborVertex]:
                minDistancesFromStart[neighborVertex] = newDistance

    return [-1 if distance == float("inf") else distance for distance in minDistancesFromStart]


def getNextClosestUnvisitedVertex(minDistancesFromStart, visited):
    candidateVertex = None
    candidateDistance = float("inf")

    for vertex, distance in enumerate(minDistancesFromStart):
        if vertex in visited:
            continue
        if distance <= candidateDistance:
            candidateVertex = vertex
            candidateDistance = distance

    return candidateVertex, candidateDistance


if __name__ == "__main__":
    sampleEdges = [
        [[1, 7]],
        [[2, 6], [3, 20], [4, 3]],
        [[3, 14]],
        [[4, 2]],
        [],
        []
    ]
    print(dijkstrasAlgorithm(0, sampleEdges))
