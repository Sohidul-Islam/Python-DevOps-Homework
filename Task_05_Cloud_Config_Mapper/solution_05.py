#!/usr/bin/env python3
"""
Task 5: The Cloud Config Mapper
Manage VM configuration using dictionaries
"""

# Create a Virtual Machine dictionary
vm = {
    "id": "i-0123456789abcdef",
    "ip": "192.168.1.100",
    "status": "running",
    "region": "us-east-1"
}

print("Original VM configuration:")
print(vm)

# Update the status from "running" to "stopped"
vm["status"] = "stopped"

# Add a new key "instance_type" with value "t3.large"
vm["instance_type"] = "t3.large"

print("\nUpdated VM configuration:")
print(vm)

# Pretty print using json module
import json
print("\nFormatted VM configuration (JSON-like):")
print(json.dumps(vm, indent=2))
