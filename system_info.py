import platform
import os
from datetime import datetime

def show_system_info():
    """Display system information"""
    print("\n=== System Information ===")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Python Version: {platform.python_version()}")
    print(f"Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Current Directory: {os.getcwd()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    
    # Disk usage simulation
    try:
        total, used, free = 1000, 650, 350  # in GB (simulated)
        print(f"\nDisk Usage: {used}GB used / {total}GB total ({(used/total)*100:.1f}%)")
    except:
        pass

if __name__ == "__main__":
    show_system_info()
