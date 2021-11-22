import networkx as nx

# Example graph:
# Example 1: our class example:
G1 = nx.Graph()
G1.add_node("a")
G1.add_node("b")
G1.add_node("c")
G1.add_node("d")
G1.add_edge("a", "b", weight=3)
G1.add_edge("a", "c", weight=5)
G1.add_edge("a", "d", weight=10)
G1.add_edge("b", "c", weight=1)
G1.add_edge("b", "d", weight=4)
G1.add_edge("c", "d", weight=1)

# Example 2: simple graph:
G2 = nx.Graph()
G2.add_node("a")
G2.add_node("b")
G2.add_node("c")
G2.add_edge("a", "b", weight=1)
G2.add_edge("a", "c", weight=3)
G2.add_edge("b", "c", weight=1)

# Example 3: all path from "a" to "d" are the same length of 2:
G3 = nx.Graph()
G3.add_node("a")
G3.add_node("b")
G3.add_node("c")
G3.add_node("d")
G3.add_edge("a", "b", weight=1)
G3.add_edge("a", "c", weight=1)
G3.add_edge("a", "d", weight=2)
G3.add_edge("b", "c", weight=0)
G3.add_edge("b", "d", weight=1)
G3.add_edge("c", "d", weight=1)

# Example 4: a large graph:
G4 = nx.Graph()
G4.add_node("a")
G4.add_node("b")
G4.add_node("c")
G4.add_node("d")
G4.add_node("e")
G4.add_node("f")
G4.add_node("g")
G4.add_node("h")

G4.add_edge("a", "b", weight=3)
G4.add_edge("d", "b", weight=1)
G4.add_edge("a", "d", weight=1)
G4.add_edge("b", "c", weight=3)
G4.add_edge("e", "b", weight=1)
G4.add_edge("e", "f", weight=3)
G4.add_edge("a", "b", weight=3)
G4.add_edge("e", "c", weight=1)
G4.add_edge("c", "f", weight=1)
G4.add_edge("c", "g", weight=3)
G4.add_edge("f", "g", weight=1)
G4.add_edge("g", "h", weight=1)
G4.add_edge("f", "h", weight=3)

# Example 5: if you remove one node there is no path:
G5 = nx.Graph()
G5.add_node("a")
G5.add_node("b")
G5.add_node("c")

G5.add_edge("a", "b", weight=1)
G5.add_edge("b", "c", weight=2)

MAX_VALUE_NO_PATH = -10000


def print_payment(n1, n2, pay):
    print("the edge: {}{} need to pay: {}".format(n1, n2, pay))


def check_if_it_on_the_shortest_path(n1, n2, path_list):
    for i in range(len(path_list)):
        if path_list[i] == n1:
            if path_list[i + 1] == n2:
                return True
    return False


def vcg_cheapest_path(graph, source, target):
    """Return the payment of eech edge on the graph by the vcg algorithms.
        Example 1: our class example
        >>> vcg_cheapest_path(G1, "a", "d")
        the edge: ab need to pay: -4
        the edge: ac need to pay: 0
        the edge: ad need to pay: 0
        the edge: bc need to pay: -2
        the edge: bd need to pay: 0
        the edge: cd need to pay: -3

        Example 2: simple graph
        >>> vcg_cheapest_path(G2, "a", "c")
        the edge: ab need to pay: -2
        the edge: ac need to pay: 0
        the edge: bc need to pay: -2

        Example 3: all path from "a" to "d" are the same length of 2.
        >>> vcg_cheapest_path(G3, "a", "d")
        the edge: ab need to pay: 0
        the edge: ac need to pay: 0
        the edge: ad need to pay: -2
        the edge: bc need to pay: 0
        the edge: bd need to pay: 0
        the edge: cd need to pay: 0

        # Example 4: a large graph:
        >>> vcg_cheapest_path(G4, "a", "h")
        the edge: ab need to pay: 0
        the edge: ad need to pay: -2
        the edge: bd need to pay: 0
        the edge: bc need to pay: 0
        the edge: be need to pay: -2
        the edge: ce need to pay: 0
        the edge: cf need to pay: -2
        the edge: cg need to pay: 0
        the edge: ef need to pay: 0
        the edge: fg need to pay: -2
        the edge: fh need to pay: 0
        the edge: gh need to pay: -2

        # Example 5: if you remove one node there is no path:
        >>> vcg_cheapest_path(G5, "a", "c")
        the edge: ab need to pay: -10000
        the edge: bc need to pay: -10000


            """

    dijkstra_path_list = nx.dijkstra_path(graph, source, target)
    dijkstra_length = nx.dijkstra_path_length(graph, source, target)

    for n1, n2 in graph.edges:
        w = graph.edges[n1, n2]['weight']
        graph.remove_edge(n1, n2)
        try:
            tmp_dijkstra_path_length = nx.dijkstra_path_length(graph, source, target)
            if check_if_it_on_the_shortest_path(n1, n2, dijkstra_path_list):
                pay = (-tmp_dijkstra_path_length) - (-dijkstra_length + w)
                print_payment(n1, n2, pay)
            else:
                print_payment(n1, n2, 0)
        except nx.NetworkXNoPath:
            print_payment(n1, n2, MAX_VALUE_NO_PATH)
        finally:
            graph.add_edge(n1, n2, weight=w)


if __name__ == '__main__':
    import doctest
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))

