from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

def h_mannhatan(node_state, end_state):
    x1, y1 = node_state
    x2, y2 = end_state
    return abs(x1 - x2) + abs(y1 - y2)

class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

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
        frontier.add(node,node.cost +  h_mannhatan(node.state, grid.end))

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

                    for estado,costo in neighbours.items():
                        if costo not in explored:
                            new_node = Node(estado, costo, node.cost + grid.get_cost(costo))
                            new_node.parent = node
                            frontier.add(new_node, new_node.cost + h_mannhatan(new_node.state, grid.end))
                            explored[new_node.state] = new_node.cost 

                    print(explored)
        return NoSolution(explored)
