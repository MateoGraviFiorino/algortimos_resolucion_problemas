from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {} 
        
        # Add the node to the explored dictionary
        explored[node.state] = True
        
        # TAD Priority Queue
        frontier = PriorityQueueFrontier()
        frontier.add(node, node.cost)


        # Add the node to the explored dictionary
        explored[node.state] = node.cost
        
        
        while True: 

                    #  Fail if the frontier is empty
                    if frontier.is_empty():
                        return NoSolution(explored) 

                    # Return if the node contains a goal state
                    if node.state == grid.end:
                        return Solution(node, explored) 

                    node = frontier.pop()
                    # Mark the node as explored
                    explored[node.state] = node.cost #guardo el nodo explorado

                    # BFS
                    neighbours = grid.get_neighbours(node.state)

                    for k,v in neighbours.items():
                        if v not in explored:
                            new_node = Node(k, v, node.cost + grid.get_cost(v))
                            new_node.parent = node
                            frontier.add(new_node, new_node.cost)
                            explored[new_node.state] = new_node.cost 

                    print(explored)


        return NoSolution(explored)
