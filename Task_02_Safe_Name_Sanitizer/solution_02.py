#!/usr/bin/env python3
"""
Task 2: The "Safe Name" Sanitizer
Sanitize bucket names for cloud providers
"""

# Original bucket name
bucket_name = "My Project Backup"

print(f"Original name: '{bucket_name}'")

# Step 1: Strip whitespace from beginning and end
sanitized = bucket_name.strip()

# Step 2: Replace spaces with hyphens
sanitized = sanitized.replace(" ", "-")

# Step 3: Convert to lowercase
sanitized = sanitized.lower()

print(f"Sanitized name: '{sanitized}'")

# One-liner version
bucket_name_2 = "  My Project Backup  "
sanitized_oneliner = bucket_name_2.strip().replace(" ", "-").lower()
print(f"One-liner result: '{sanitized_oneliner}'")
