import tkinter as tk
from tkinter import ttk

class ControlPanel(ttk.Frame):
    def __init__(self, parent, start_callback, pause_callback, step_callback, speed_callback):
        super().__init__(parent)
        
        # Control buttons
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.start_button = ttk.Button(
            self.button_frame,
            text="Start",
            command=start_callback
        )
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.pause_button = ttk.Button(
            self.button_frame,
            text="Pause",
            command=pause_callback
        )
        self.pause_button.pack(side=tk.LEFT, padx=5)
        
        self.step_button = ttk.Button(
            self.button_frame,
            text="Step",
            command=step_callback
        )
        self.step_button.pack(side=tk.LEFT, padx=5)
        
        # Speed control
        self.speed_frame = ttk.Frame(self)
        self.speed_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(self.speed_frame, text="Speed:").pack(side=tk.LEFT)
        
        self.speed_scale = ttk.Scale(
            self.speed_frame,
            from_=0.1,
            to=2.0,
            orient=tk.HORIZONTAL,
            command=speed_callback
        )
        self.speed_scale.set(1.0)
        self.speed_scale.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)