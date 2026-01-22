#!/usr/bin/env python3
# Task 6: Log File Duplicator - Create test copies of log files

import os
import shutil

source_file = "app.log"

# Create sample log file if it doesn't exist
if not os.path.exists(source_file):
    with open(source_file, "w") as f:
        f.write("2026-01-22 18:34:00 INFO Application started\n")
        f.write("2026-01-22 18:34:01 INFO Connected to database\n")
        f.write("2026-01-22 18:34:02 WARNING High memory usage detected\n")
        f.write("2026-01-22 18:34:03 ERROR Failed to connect to external API\n")
        f.write("2026-01-22 18:34:04 INFO Request processed successfully\n")
    print(f"Created sample file: {source_file}")

# Make 5 copies
for i in range(1, 6):
    destination_file = f"app_{i}.log"
    shutil.copy(source_file, destination_file)
    print(f"Created copy: {destination_file}")

print("\nAll copies created successfully!")

# Show all log files
log_files = [f for f in os.listdir(".") if f.endswith(".log")]
print(f"\nTotal log files in directory: {len(log_files)}")
print(f"Files: {sorted(log_files)}")
