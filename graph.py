class Graph:
    def __init__(self) -> None:
        self.adjacency_list :dict[str, list[list[str|int]]] = {}

    def add_vertex(self, Vid:str) -> None:
        self.adjacency_list[Vid] = []
    
    def add_edge(self, src:str, dest:str, edge:int) -> None:
        self.adjacency_list[src].append([dest, edge])