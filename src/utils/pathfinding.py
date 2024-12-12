from collections import deque

def find_path(warehouse, start, end):
    """Simple BFS pathfinding algorithm"""
    if not (warehouse.is_valid_position(*start) and warehouse.is_valid_position(*end)):
        return None

    queue = deque([(start, [])])
    visited = {start}
    
    # Possible movements: up, right, down, left
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        (x, y), path = queue.popleft()
        
        if (x, y) == end:
            return path + [(x, y)]

        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            next_pos = (next_x, next_y)

            if (warehouse.is_valid_position(next_x, next_y) and 
                next_pos not in visited):
                queue.append((next_pos, path + [(x, y)]))
                visited.add(next_pos)

    return None