#!/usr/bin/env python3
"""
Task 9: The Path Builder
Build cross-platform file paths
"""

import os
from pathlib import Path

# Define path components
base_dir = "/var/log"
app_name = "nginx"
filename = "access.log"

# Method 1: Using os.path.join
full_path = os.path.join(base_dir, app_name, filename)
print(f"Using os.path.join: {full_path}")

# Method 2: Using pathlib (more modern approach)
full_path_pathlib = Path(base_dir) / app_name / filename
print(f"Using pathlib: {full_path_pathlib}")

# Show current platform
print(f"\nCurrent OS: {os.name}")
print(f"Path separator: '{os.sep}'")

# Example with Windows-style paths
print("\n--- Windows Example ---")
base_dir_win = "C:\\Program Files"
app_name_win = "MyApp"
filename_win = "config.ini"

win_path = os.path.join(base_dir_win, app_name_win, filename_win)
print(f"Windows path: {win_path}")

# Pathlib automatically handles platform differences
win_path_pathlib = Path(base_dir_win) / app_name_win / filename_win
print(f"Pathlib (auto-platform): {win_path_pathlib}")

# Additional useful path operations
print("\n--- Useful Path Operations ---")
example_path = Path(base_dir) / app_name / filename
print(f"Parent directory: {example_path.parent}")
print(f"Filename: {example_path.name}")
print(f"File extension: {example_path.suffix}")
print(f"Filename without extension: {example_path.stem}")
