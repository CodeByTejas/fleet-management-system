import tkinter as tk
from tkinter import ttk

class StatusPanel(ttk.Frame):
    def __init__(self, parent, warehouse):
        super().__init__(parent)
        self.warehouse = warehouse
        
        # Robot Status
        self.robot_frame = ttk.LabelFrame(self, text="Robot Status")
        self.robot_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.robot_text = tk.Text(self.robot_frame, height=5, width=40)
        self.robot_text.pack(padx=5, pady=5)
        
        # Task Status
        self.task_frame = ttk.LabelFrame(self, text="Task Status")
        self.task_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.task_text = tk.Text(self.task_frame, height=5, width=40)
        self.task_text.pack(padx=5, pady=5)
        
    def update_status(self):
        """Update status display"""
        # Update robot status
        self.robot_text.delete(1.0, tk.END)
        for robot in self.warehouse.robots.values():
            self.robot_text.insert(tk.END, f"{str(robot)}\n")
            
        # Update task status
        self.task_text.delete(1.0, tk.END)
        for task in self.warehouse.tasks.values():
            self.task_text.insert(tk.END, f"{str(task)}\n")