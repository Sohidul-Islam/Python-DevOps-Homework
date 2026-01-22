#!/usr/bin/env python3
# Task 5: Cloud Config Mapper - Update VM configuration

vm = {
    "id": "i-0123456789abcdef",
    "ip": "192.168.1.100",
    "status": "running",
    "region": "us-east-1"
}

print("Original VM configuration:")
print(vm)

# Update status
vm["status"] = "stopped"

# Add instance type
vm["instance_type"] = "t3.large"

print("\nUpdated VM configuration:")
print(vm)

# Pretty print
import json
print("\nFormatted VM configuration (JSON-like):")
print(json.dumps(vm, indent=2))
