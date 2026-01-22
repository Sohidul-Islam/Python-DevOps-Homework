#!/usr/bin/env python3
# Task 3: Port Validator - Check if port numbers are valid

port_string = "8080"

# Convert to integer
port = int(port_string)

# Check if it's in the valid range
if 1 <= port <= 65535:
    print("Valid")
else:
    print("Invalid")

# Test with different ports
test_ports = ["8080", "80", "443", "0", "65535", "65536", "100000"]

print("\nTesting multiple ports:")
for port_str in test_ports:
    port_num = int(port_str)
    if 1 <= port_num <= 65535:
        print(f"Port {port_str}: Valid")
    else:
        print(f"Port {port_str}: Invalid")
