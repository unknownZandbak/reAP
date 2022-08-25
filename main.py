from graph import Graph

def setup_graph() -> Graph:

    graph = Graph()

    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")
    graph.add_vertex("G")
    graph.add_vertex("H")
    graph.add_vertex("I")
    graph.add_vertex("J")

    # A
    graph.add_edge("A", "B", 2)
    graph.add_edge("A", "J", 5)
    # B
    graph.add_edge("B", "A", 2)
    graph.add_edge("B", "C", 4)
    graph.add_edge("B", "D", 1)
    # C
    graph.add_edge("C", "B", 4)
    graph.add_edge("C", "D", 3)
    graph.add_edge("C", "E", 2)
    # D
    graph.add_edge("D", "B", 1)
    graph.add_edge("D", "C", 3)
    graph.add_edge("D", "E", 1)
    graph.add_edge("D", "F", 4)
    graph.add_edge("D", "G", 3)
    # E
    graph.add_edge("E", "C", 2)
    graph.add_edge("E", "D", 1)
    graph.add_edge("E", "F", 6)
    # F
    graph.add_edge("F", "E", 6)
    graph.add_edge("F", "D", 4)
    graph.add_edge("F", "G", 10)
    # G
    graph.add_edge("G", "D", 3)
    graph.add_edge("G", "F", 10)
    graph.add_edge("G", "H", 2)
    graph.add_edge("G", "I", 5)
    # H
    graph.add_edge("H", "G", 2)
    graph.add_edge("H", "I", 3)
    # I
    graph.add_edge("I", "G", 5)
    graph.add_edge("I", "H", 3)
    graph.add_edge("I", "J", 4)
    # J
    graph.add_edge("J", "A", 5)
    graph.add_edge("J", "I", 4)

    return graph

def dijkstra(graph:Graph, src:str, dest:str) -> list[str]:
    
    prio_que = dijkstra_exploration(graph, src, dest)

    # back tracking
    result = [dest]

    while result[-1] != src:
        via = prio_que[result[-1]][0]
        result.append(via)

    result.reverse()
    return result

def dijkstra_exploration(graph:Graph, src:str, dest:str):
    discoverd = {}
    priority_queue = {src: [src, 0]}

    # exploration
    while dest not in priority_queue:
        node, (via, cost) = list(priority_queue.items())[0]
        for neighbour, stepcost in graph.adjacency_list[node]:
            if neighbour not in discoverd:
                if neighbour in priority_queue.keys():
                    if stepcost+cost < priority_queue[neighbour][1]:
                        priority_queue[neighbour] = [node, stepcost+cost]
                    else: continue
                else: priority_queue[neighbour] = [node, stepcost+cost]
                
                if neighbour == dest:
                    discoverd[node] = [via, cost]
                    discoverd[neighbour] = [node, stepcost+cost]
                    return discoverd
            else: continue

        discoverd[node] = [via, cost]
        priority_queue.pop(node)
        priority_queue = dict(sorted(priority_queue.items(), key=lambda x:x[1][1]))

def main():
    graph = setup_graph()
    result = dijkstra(graph, "A", "H")

if __name__ == '__main__' :
    main()