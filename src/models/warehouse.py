class Warehouse:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.robots = {}
        self.tasks = {}
        self.obstacles = set()

    def add_robot(self, robot):
        self.robots[robot.id] = robot
        self.grid[robot.y][robot.x] = 'R'

    def add_task(self, task):
        self.tasks[task.id] = task

    def add_obstacle(self, x, y):
        self.obstacles.add((x, y))
        self.grid[y][x] = 'X'

    def is_valid_position(self, x, y):
        return (0 <= x < self.width and 
                0 <= y < self.height and 
                (x, y) not in self.obstacles)

    def display(self):
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in self.obstacles:
                    print('X', end=' ')
                elif any(robot.x == x and robot.y == y for robot in self.robots.values()):
                    print('R', end=' ')
                else:
                    print('.', end=' ')
            print()