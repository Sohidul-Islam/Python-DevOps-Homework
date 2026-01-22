#!/usr/bin/env python3
# Task 7: Prod Guard - Prevent dangerous operations in production

env = "production"

# Check environment before deleting
if env != "production":
    print("Executing Delete")
else:
    print("Access Denied: Cannot delete in Prod!")

# Test with different environments
print("\nTesting with different environments:")

environments = ["development", "staging", "production", "test"]

for environment in environments:
    print(f"\nEnvironment: {environment}")
    if environment != "production":
        print("  OK - Executing Delete")
    else:
        print("  BLOCKED - Access Denied: Cannot delete in Prod!")

# Better version that handles variations
print("\n--- Enhanced Version ---")

def can_delete(env):
    protected_envs = ["production", "prod"]
    
    if env.lower() in protected_envs:
        return False
    return True

test_envs = ["production", "PRODUCTION", "prod", "development", "dev"]

for test_env in test_envs:
    if can_delete(test_env):
        print(f"{test_env}: ✓ Executing Delete")
    else:
        print(f"{test_env}: ✗ Access Denied: Cannot delete in Prod!")
