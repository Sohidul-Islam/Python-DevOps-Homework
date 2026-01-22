#!/usr/bin/env python3
"""
Task 1: The Domain Extractor
Extract domain name from a URL using string manipulation
"""

# Given URL
url = "https://api.github.com/v3"

# Method 1: Using split()
# Remove protocol (https://)
without_protocol = url.split("://")[1]  # "api.github.com/v3"

# Split by "/" and get the first part
full_domain = without_protocol.split("/")[0]  # "api.github.com"

# Split by "." and get the last two parts (domain.com)
parts = full_domain.split(".")
domain = ".".join(parts[-2:])  # "github.com"

print(f"Extracted domain: {domain}")

# Method 2: Alternative using replace and split
url2 = "https://api.github.com/v3"
cleaned = url2.replace("https://", "").replace("http://", "")
domain_with_path = cleaned.split("/")[0]
domain_parts = domain_with_path.split(".")
domain_name = ".".join(domain_parts[-2:])

print(f"Extracted domain (Method 2): {domain_name}")
