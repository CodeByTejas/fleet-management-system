class Robot:
    def __init__(self, robot_id, x, y):
        self.id = robot_id
        self.x = x
        self.y = y
        self.status = "idle"  # idle, moving, executing_task
        self.current_task = None
        self.path = []

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def assign_task(self, task):
        self.current_task = task
        self.status = "moving"

    def complete_task(self):
        self.current_task = None
        self.status = "idle"

    def __str__(self):
        return f"Robot {self.id} at ({self.x}, {self.y}) - {self.status}"