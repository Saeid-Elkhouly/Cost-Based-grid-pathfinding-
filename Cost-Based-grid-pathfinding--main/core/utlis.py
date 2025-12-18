directions = [(-1,0), (1,0), (0,-1), (0,1)] #up, down, left, right
def is_valid(pos, grid):
    row, col = pos
    rows, cols = len(grid), len(grid[0]) if grid else (0,0)
    return 0 <= row < rows and 0 <= col < cols and grid[row][col] != 0

def get_neighbors(pos, grid):
    neighbors = []
    for dr, dc in directions:
        new_pos = (pos[0]+dr, pos[1]+dc)
        if is_valid(new_pos, grid):
            cost = grid[new_pos[0]][new_pos[1]]
            neighbors.append((new_pos, cost))
    return neighbors  # list of of cells that can be reached from the current cell wuth the given cost قامةالمربعات الي ممكن نتحرك ليها مع تكلفة كل مربع

def reconstruct_path(node):    #start =(0,0) parent in node = none في تعريف ال node نفسه فوق
    path = []
    current = node
    while current:
        path.append(current.position)
        current = current.parent
    return path[::-1]  #reverse the path

def manhattan(pos, goal):
    return abs(pos[0]-goal[0]) + abs(pos[1]-goal[1])
