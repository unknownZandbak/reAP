from unittest import TestCase
import main


class testDijkstraAlgo(TestCase):
    
    graph = main.setup_graph()

    def test_dijkstra1(self):

        r1 = main.dijkstra(self.graph, "A", "H")
        self.assertSequenceEqual(["A", "B", "D", "G", "H"], r1)

    def test_dijkstra2(self):

        r2 = main.dijkstra(self.graph, "C", "I")
        self.assertSequenceEqual(["C", "D", "G", "I"], r2)

    def test_dijkstra3(self):

        r3 = main.dijkstra(self.graph, "J", "F")
        self.assertSequenceEqual(["J", "A", "B", "D", "F"], r3)

    def test_dijkstra4(self):

        r4 = main.dijkstra(self.graph, "I", "C")
        self.assertSequenceEqual(["I", "G", "D", "C"], r4)

    def test_dijkstra5(self):

        r5 = main.dijkstra(self.graph, "E", "A")
        self.assertSequenceEqual(["E", "D", "B", "A"], r5)

    def test_dijkstra6(self):

        r2 = main.dijkstra(self.graph, "C", "J")
        self.assertSequenceEqual(['C', 'B', 'A', 'J'], r2)