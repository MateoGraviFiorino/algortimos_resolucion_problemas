from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points
            
        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {} 

        #Create frontier
        frontier=StackFrontier()
        frontier.add(node)
    
        
        # Add the node to the explored dictionary
        explored[node.state] = True


        while True:
            if frontier.is_empty():
                return NoSolution(explored)

             #guardo el nodo explorado
            node = frontier.remove()
        
            explored[node.state] = True

            # Return if the node contains a goal state
            if node.state == grid.end:
                return Solution(node, explored) 
            
            #DFS
            neighbours = grid.get_neighbours(node.state)
            print(neighbours)

            for k, v in neighbours.items():
                if v not in explored:
                    new_node = Node(k, v, node.cost + grid.get_cost(v))
                    new_node.parent = node
                    frontier.add(new_node)
                    explored[v] = True

            print(explored)