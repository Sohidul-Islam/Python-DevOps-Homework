#!/usr/bin/env python3
# Task 1: Domain Extractor - Extract domain from URL

url = "https://api.github.com/v3"

# Remove the protocol part
without_protocol = url.split("://")[1]

# Get just the domain part (before the path)
full_domain = without_protocol.split("/")[0]

# Extract the main domain (last two parts)
parts = full_domain.split(".")
domain = ".".join(parts[-2:])

print(f"Extracted domain: {domain}")

# Alternative approach
url2 = "https://api.github.com/v3"
cleaned = url2.replace("https://", "").replace("http://", "")
domain_with_path = cleaned.split("/")[0]
domain_parts = domain_with_path.split(".")
domain_name = ".".join(domain_parts[-2:])

print(f"Extracted domain (Method 2): {domain_name}")
