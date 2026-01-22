#!/usr/bin/env python3
# Task 4: Fleet Inventory - Get first and last servers

servers = ["web01", "db01", "app01", "web02"]

# Get first and last elements
web_servers = [servers[0], servers[-1]]

print(f"Original servers: {servers}")
print(f"Web servers (first and last): {web_servers}")

# Alternative way
web_servers_alt = [servers[i] for i in [0, -1]]
print(f"Web servers (alternative): {web_servers_alt}")

# Bonus: split the fleet in half
half_count = len(servers) // 2
first_half = servers[:half_count]
print(f"\nFirst 50% of servers: {first_half}")

last_half = servers[half_count:]
print(f"Last 50% of servers: {last_half}")
