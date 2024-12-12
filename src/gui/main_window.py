import tkinter as tk
from tkinter import ttk
from .warehouse_canvas import WarehouseCanvas
from .status_panel import StatusPanel
from .control_panel import ControlPanel

class MainWindow(tk.Tk):
    def __init__(self, fleet_manager):
        super().__init__()
        
        self.fleet_manager = fleet_manager
        self.running = False
        self.speed = 1.0
        
        self.title("Fleet Management System")
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the main UI components"""
        # Main container
        main_container = ttk.Frame(self)
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left panel (Warehouse visualization)
        left_panel = ttk.Frame(main_container)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.warehouse_canvas = WarehouseCanvas(left_panel, self.fleet_manager.warehouse)
        self.warehouse_canvas.pack(padx=5, pady=5)
        
        # Right panel (Status and Controls)
        right_panel = ttk.Frame(main_container)
        right_panel.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Status panel
        self.status_panel = StatusPanel(right_panel, self.fleet_manager.warehouse)
        self.status_panel.pack(fill=tk.X)
        
        # Control panel
        self.control_panel = ControlPanel(
            right_panel,
            self.start_simulation,
            self.pause_simulation,
            self.step_simulation,
            self.update_speed
        )
        self.control_panel.pack(fill=tk.X)
        
        # Initial display
        self.update_display()
        
    def start_simulation(self):
        """Start the simulation"""
        self.running = True
        self.run_simulation()
        
    def pause_simulation(self):
        """Pause the simulation"""
        self.running = False
        
    def step_simulation(self):
        """Perform one simulation step"""
        self.fleet_manager.assign_tasks()
        self.fleet_manager.update()
        self.update_display()
        
    def update_speed(self, value):
        """Update simulation speed"""
        self.speed = float(value)
        
    def run_simulation(self):
        """Main simulation loop"""
        if self.running:
            self.step_simulation()
            self.after(int(1000 / self.speed), self.run_simulation)
            
    def update_display(self):
        """Update all display components"""
        self.warehouse_canvas.update_display()
        self.status_panel.update_status()