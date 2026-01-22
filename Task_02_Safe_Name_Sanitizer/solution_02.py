#!/usr/bin/env python3
# Task 2: Safe Name Sanitizer - Make cloud-friendly bucket names

bucket_name = "My Project Backup"

print(f"Original name: '{bucket_name}'")

# Clean it up for cloud providers
sanitized = bucket_name.strip()
sanitized = sanitized.replace(" ", "-")
sanitized = sanitized.lower()

print(f"Sanitized name: '{sanitized}'")

# Can also do it in one line
bucket_name_2 = "  My Project Backup  "
sanitized_oneliner = bucket_name_2.strip().replace(" ", "-").lower()
print(f"One-liner result: '{sanitized_oneliner}'")
