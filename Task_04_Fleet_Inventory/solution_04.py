#!/usr/bin/env python3
"""
Task 4: The Fleet Inventory
Extract subsets of servers using list slicing
"""

# Original server list
servers = ["web01", "db01", "app01", "web02"]

# Method 1: Using slicing to get first and last elements
web_servers = [servers[0], servers[-1]]

print(f"Original servers: {servers}")
print(f"Web servers (first and last): {web_servers}")

# Method 2: Using slicing with step
# Get first element and last element using list comprehension
web_servers_alt = [servers[i] for i in [0, -1]]
print(f"Web servers (alternative): {web_servers_alt}")

# Bonus: Get first 50% of servers
half_count = len(servers) // 2
first_half = servers[:half_count]
print(f"\nFirst 50% of servers: {first_half}")

# Bonus: Get last 50% of servers
last_half = servers[half_count:]
print(f"Last 50% of servers: {last_half}")
