import tkinter as tk
from tkinter import ttk

class WarehouseCanvas(tk.Canvas):
    def __init__(self, parent, warehouse, cell_size=40):
        self.cell_size = cell_size
        width = warehouse.width * cell_size
        height = warehouse.height * cell_size
        
        super().__init__(
            parent, 
            width=width, 
            height=height, 
            bg='white',
            highlightthickness=1,
            highlightbackground='gray'
        )
        
        self.warehouse = warehouse
        self.robot_shapes = {}
        self.task_shapes = {}
        
    def draw_grid(self):
        """Draw the warehouse grid"""
        # Clear previous drawings
        self.delete('grid_line')
        
        # Draw vertical lines
        for i in range(self.warehouse.width + 1):
            x = i * self.cell_size
            self.create_line(
                x, 0, x, self.warehouse.height * self.cell_size,
                fill='gray', tags='grid_line'
            )
            
        # Draw horizontal lines
        for i in range(self.warehouse.height + 1):
            y = i * self.cell_size
            self.create_line(
                0, y, self.warehouse.width * self.cell_size, y,
                fill='gray', tags='grid_line'
            )
            
    def draw_obstacles(self):
        """Draw warehouse obstacles"""
        self.delete('obstacle')
        for x, y in self.warehouse.obstacles:
            self.create_rectangle(
                x * self.cell_size,
                y * self.cell_size,
                (x + 1) * self.cell_size,
                (y + 1) * self.cell_size,
                fill='gray',
                tags='obstacle'
            )
            
    def draw_robots(self):
        """Draw robots on the canvas"""
        # Clear previous robot shapes
        for shape_id in self.robot_shapes.values():
            self.delete(shape_id)
        self.robot_shapes.clear()
        
        # Draw each robot
        for robot in self.warehouse.robots.values():
            x = robot.x * self.cell_size + self.cell_size/2
            y = robot.y * self.cell_size + self.cell_size/2
            
            # Different colors based on robot status
            color = {
                'idle': 'green',
                'moving': 'blue',
                'executing_task': 'orange'
            }.get(robot.status, 'black')
            
            # Create robot circle
            robot_id = self.create_oval(
                x - self.cell_size/3,
                y - self.cell_size/3,
                x + self.cell_size/3,
                y + self.cell_size/3,
                fill=color,
                tags='robot'
            )
            
            # Add robot number
            self.create_text(
                x, y,
                text=str(robot.id),
                fill='white',
                font=('Arial', int(self.cell_size/3)),
                tags='robot'
            )
            
            self.robot_shapes[robot.id] = robot_id
            
    def draw_tasks(self):
        """Draw task start and end positions"""
        # Clear previous task shapes
        for shape_id in self.task_shapes.values():
            self.delete(shape_id)
        self.task_shapes.clear()
        
        # Draw each task
        for task in self.warehouse.tasks.values():
            # Draw start position (green square)
            start_x = task.start_pos[0] * self.cell_size + self.cell_size/2
            start_y = task.start_pos[1] * self.cell_size + self.cell_size/2
            
            start_shape = self.create_rectangle(
                start_x - self.cell_size/4,
                start_y - self.cell_size/4,
                start_x + self.cell_size/4,
                start_y + self.cell_size/4,
                fill='lightgreen' if task.status == 'pending' else 'gray',
                tags='task'
            )
            
            # Draw end position (red square)
            end_x = task.end_pos[0] * self.cell_size + self.cell_size/2
            end_y = task.end_pos[1] * self.cell_size + self.cell_size/2
            
            end_shape = self.create_rectangle(
                end_x - self.cell_size/4,
                end_y - self.cell_size/4,
                end_x + self.cell_size/4,
                end_y + self.cell_size/4,
                fill='red' if task.status != 'completed' else 'gray',
                tags='task'
            )
            
            self.task_shapes[task.id] = (start_shape, end_shape)
            
    def update_display(self):
        """Update the entire warehouse display"""
        self.draw_grid()
        self.draw_obstacles()
        self.draw_tasks()
        self.draw_robots()