#!/usr/bin/env python3
# Task 10: Secret Masker - Hide sensitive data in logs

api_key = "AKIA1234567890EXAMPLE"

# Get first 4 characters
visible_part = api_key[:4]

# Calculate how many to mask
masked_length = len(api_key) - 4

# Create masked version
masked_key = visible_part + ("*" * masked_length)

print(f"Original API Key: {api_key}")
print(f"Masked API Key: {masked_key}")

# Flexible masking function
print("\n--- Flexible Masking Function ---")

def mask_secret(secret, visible_chars=4, mask_char="*"):
    """
    Mask a secret, showing only first few characters
    """
    if len(secret) <= visible_chars:
        return mask_char * len(secret)
    
    return secret[:visible_chars] + (mask_char * (len(secret) - visible_chars))

# Test with different secrets
secrets = [
    ("AKIA1234567890EXAMPLE", "AWS Access Key"),
    ("ghp_1234567890abcdefghijklmnopqrstuvwxyz", "GitHub Token"),
    ("sk-1234567890abcdefghijklmnopqrstuvwxyz", "OpenAI API Key"),
    ("password123", "Password")
]

for secret, description in secrets:
    print(f"{description}: {mask_secret(secret)}")

# Alternative: Show last 4 characters instead
print("\n--- Show Last 4 Characters ---")

def mask_secret_last(secret, visible_chars=4, mask_char="*"):
    """Mask secret but show last few characters"""
    if len(secret) <= visible_chars:
        return mask_char * len(secret)
    
    return (mask_char * (len(secret) - visible_chars)) + secret[-visible_chars:]

for secret, description in secrets:
    print(f"{description}: {mask_secret_last(secret)}")
