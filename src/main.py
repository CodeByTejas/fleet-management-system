from fleet_manager import FleetManager
from gui.main_window import MainWindow

def main():
    # Initialize the fleet management system
    manager = FleetManager()
    
    # Create some sample tasks
    manager.create_task(1, (0, 5), (9, 5))
    manager.create_task(2, (5, 0), (5, 9))
    
    # Create and run the GUI
    app = MainWindow(manager)
    app.mainloop()

if __name__ == "__main__":
    main()