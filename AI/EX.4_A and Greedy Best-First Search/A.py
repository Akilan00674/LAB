import heapq

# Movement directions: up, down, left, right
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position  # (row, col)
        self.parent = parent
        self.g = g                # cost from start
        self.h = h                # estimated cost to goal
        self.f = g + h            # total cost

    def __lt__(self, other):
        return self.f < other.f # to find the min node

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0]) # to find lenght
    open_list = [] # to save a q
    closed_set = set() # already visied

    start_node = Node(start, None, 0, heuristic(start, goal)) # starting node
    heapq.heappush(open_list, start_node) # push to open list 

    while open_list: # Keep running the loop as long as there are nodes to check in the open list.
        current_node = heapq.heappop(open_list) # Lowest total cost
        current_pos = current_node.position #  Gets the (row, col)

        if current_pos == goal: # Have we reached the goal?
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_pos) # marks the current position as already visited

        for move in moves:
            neighbor = (current_pos[0] + move[0], current_pos[1] + move[1])
            if (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and
                grid[neighbor[0]][neighbor[1]] == 0 and neighbor not in closed_set):
                """
Inside the grid boundaries.

Not a wall (grid value is 0 means walkable).

Not already visited (closed_set).

                """

                g = current_node.g + 1
                h = heuristic(neighbor, goal)
                neighbor_node = Node(neighbor, current_node, g, h)

                if all(neighbor != n.position or neighbor_node.f < n.f for n in open_list):
                    heapq.heappush(open_list, neighbor_node)

    return None  # No path found

# ---------------- Test Case ----------------
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0]
]

start = (0, 0)
goal = (3, 4)

path = a_star(grid, start, goal)
print("A* Shortest Path:")
print(path if path else "No path found.")