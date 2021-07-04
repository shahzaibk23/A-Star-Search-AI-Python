from icecream import ic
nodes = ['A', 'B','C','F','O','P','R','S']
weightedEdges = [
    ["Oradea","Zerind",71],
    ["Oradea","Sibiu",151],
    ["Zerind","Arad",75],
    ["Arad","Sibiu",140],
    ["Arad","Timisoara",118],
    ["Sibiu","Fagaras",99],
    ["Sibiu","Rimnicu Vilcea",80],
    ["Timisoara","Lugoj",111],
    ["Lugoj","Mehadia",70],
    ["Mehadia","Dobreta",75],
    ["Dobreta","Craiova",120],
    ["Rimnicu Vilcea","Craiova",146],
    ["Rimnicu Vilcea","Pitesti",97],
    ["Craiova","Pitesti",138],
    ["Pitesti","Bucharest",101],
    ["Fagaras","Bucharest",211],
    ["Bucharest","Giurgiu",90],
    ["Bucharest","Urziceni",85],
    ["Urziceni","Hirsova",98],
    ["Hirsova","Efoire",86],
    ["Urziceni","Vaslui",142],
    ["Vaslui","Iasi",92],
    ["Iasi","Neamt",87]

]
costToReachN = {
    "Arad":366,
    "Bucharest":0,
    "Craiova":160,
    "Dobreta":242,
    "Efoire":161,
    "Fagaras":176,
    "Giurgiu":77,
    "Hirsova":151,
    "Iasi":226,
    "Lugoj":244,
    "Mehadia":241,
    "Neamt":234,
    "Oradea":380,
    "Pitesti":10,
    "Rimnicu Vilcea":193,
    "Sibiu":253,
    "Timisoara":329,
    "Urziceni":80,
    "Vaslui":199,
    "Zerind":374
}

initialState = 'Arad'
goalState = 'Bucharest'

path = []
totalCost = []
heuristicCost = []

n = initialState

while n != goalState:
    neighbours = [edge for edge in weightedEdges if edge[0] == n]
    newNeighbours = [[edge[0],edge[1],edge[2] + totalCost[-1]] if n != initialState else edge for edge in neighbours]
    neighboursPlusHeuristic = [[edge[0],edge[1],edge[2],edge[2] + costToReachN[edge[1]]] for edge in newNeighbours]
    minNeighbour = [edge for edge in neighboursPlusHeuristic if edge[3] == min([ edge[3] for edge in neighboursPlusHeuristic ])][0]
    n = minNeighbour[1]
    path.append(n)
    totalCost.append(minNeighbour[2])
    heuristicCost.append(minNeighbour[3])

    print(f"Next Node is {n} at min cost: {minNeighbour[3]}")

print(f"{'-'*20}\nThe Goal Path is:{path}  \nWith Total Cost of {sum(totalCost)} \nHaving the cost of path {totalCost} \nWith Heuristic Cost {sum(heuristicCost)} \nHaving Heuristic Path {heuristicCost}")