from models.warehouse import Warehouse
from models.robot import Robot
from models.task import Task
from utils.pathfinding import find_path

class FleetManager:
    def __init__(self):
        self.warehouse = Warehouse(10, 10)  # 10x10 grid warehouse
        self.initialize_environment()

    def initialize_environment(self):
        # Add some obstacles
        obstacles = [(2, 2), (2, 3), (2, 4), (7, 5), (7, 6), (7, 7)]
        for x, y in obstacles:
            self.warehouse.add_obstacle(x, y)

        # Add robots
        robot1 = Robot(1, 0, 0)
        robot2 = Robot(2, 9, 9)
        self.warehouse.add_robot(robot1)
        self.warehouse.add_robot(robot2)

    def create_task(self, task_id, start_pos, end_pos, priority=1):
        task = Task(task_id, start_pos, end_pos, priority)
        self.warehouse.add_task(task)
        return task

    def assign_tasks(self):
        """Simple task assignment strategy"""
        for task in self.warehouse.tasks.values():
            if task.status == "pending":
                # Find nearest available robot
                nearest_robot = None
                min_distance = float('inf')
                
                for robot in self.warehouse.robots.values():
                    if robot.status == "idle":
                        distance = abs(robot.x - task.start_pos[0]) + abs(robot.y - task.start_pos[1])
                        if distance < min_distance:
                            min_distance = distance
                            nearest_robot = robot

                if nearest_robot:
                    task.assign_to_robot(nearest_robot)
                    nearest_robot.assign_task(task)
                    path = find_path(self.warehouse, (nearest_robot.x, nearest_robot.y), task.start_pos)
                    if path:
                        nearest_robot.path = path

    def update(self):
        """Update the state of all robots and tasks"""
        for robot in self.warehouse.robots.values():
            if robot.status == "moving" and robot.path:
                next_pos = robot.path.pop(0)
                robot.move_to(*next_pos)
                
                if not robot.path:  # Reached destination
                    if robot.current_task:
                        robot.current_task.complete()
                        robot.complete_task()

    def display_status(self):
        """Display the current state of the warehouse and entities"""
        print("\nWarehouse Status:")
        self.warehouse.display()
        print("\nRobots:")
        for robot in self.warehouse.robots.values():
            print(robot)
        print("\nTasks:")
        for task in self.warehouse.tasks.values():
            print(task)
        print("-" * 40)