from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position

        node = Node("", grid.start, 0)
        print(node)
        # Initialize the explored dictionary to be empty
        explored = {} 

        #Create frontier
        frontier=QueueFrontier()
        frontier.add(node)
        # Add the node to the explored dictionary
        explored[node.state] = True

        while True: 

            #  Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(explored) 

            node = frontier.remove()
            # Mark the node as explored
            explored[node.state] = True #guardo el nodo explorado

            # Return if the node contains a goal state
            if node.state == grid.end:
                return Solution(node, explored) 

            # BFS
            neighbours = grid.get_neighbours(node.state)

            for k,v in neighbours.items():
                if v not in explored:
                    new_node = Node(k, v, node.cost + grid.get_cost(v))
                    new_node.parent = node
                    frontier.add(new_node)
                    explored[v] = True

            print(explored)