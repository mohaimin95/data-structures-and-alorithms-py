def dfs(graph,src):
    stack = [src]
    while(len(stack)>0):
        current = stack.pop()
        print(current)
        for neigbors in graph.get(current,[]):
            stack.append(neigbors)

graph = {
    "a":["b","c","d"],
    "b":["e"],
    "c":[],
    "d":[],
    "e":[]
}

dfs(graph,"a")
        