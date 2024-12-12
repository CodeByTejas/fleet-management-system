class Task:
    def __init__(self, task_id, start_pos, end_pos, priority=1):
        self.id = task_id
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.priority = priority
        self.status = "pending"  # pending, assigned, completed
        self.assigned_robot = None

    def assign_to_robot(self, robot):
        self.assigned_robot = robot
        self.status = "assigned"

    def complete(self):
        self.status = "completed"

    def __str__(self):
        return f"Task {self.id}: {self.start_pos} -> {self.end_pos} ({self.status})"