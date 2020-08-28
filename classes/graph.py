from classes.node import Node

class Graph():
    nodes = []

    def add_node(self, value):
        self.nodes.append(Node(value))
                    
    def add_edge(self, initial_node_val, end_node_val):
        initial_node = [ node for node in self.nodes if node.value == initial_node_val ][0]
        end_node = [ node for node in self.nodes if node.value == end_node_val ][0]
        initial_node.add_edge(end_node)
        end_node.add_edge(initial_node)

    def bfs(self, start, value):
        start_node = [ node for node in self.nodes if node.value == start ][0]
        list_of_nodes = [start_node]

        start_node = 

        
            
            

