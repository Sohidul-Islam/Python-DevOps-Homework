#!/usr/bin/env python3
"""
Task 8: The Threshold Alert
Format monitoring metrics for human-readable alerts
"""

# CPU load from monitoring tool
cpu_load = 0.88

# Format as percentage using f-string
percentage = f"{cpu_load * 100:.0f}%"
print(f"CPU Load: {percentage}")

# More detailed alert message
alert_message = f"⚠️  ALERT: CPU usage is at {cpu_load * 100:.0f}%"
print(alert_message)

# Different formatting options
print("\n--- Different Formatting Options ---")

# With decimal places
print(f"With 1 decimal: {cpu_load * 100:.1f}%")
print(f"With 2 decimals: {cpu_load * 100:.2f}%")

# Complete monitoring alert system
print("\n--- Complete Alert System ---")

def generate_alert(metric_name, value, threshold, unit="%"):
    """Generate formatted alert message"""
    percentage = value * 100
    
    if percentage >= threshold:
        status = "🔴 CRITICAL"
    elif percentage >= threshold * 0.8:
        status = "⚠️  WARNING"
    else:
        status = "✅ OK"
    
    return f"{status}: {metric_name} is at {percentage:.0f}{unit} (Threshold: {threshold}%)"

# Test with different metrics
metrics = [
    ("CPU Load", 0.88, 80),
    ("Memory Usage", 0.65, 80),
    ("Disk Usage", 0.95, 90),
    ("Network Usage", 0.45, 70)
]

for metric_name, value, threshold in metrics:
    print(generate_alert(metric_name, value, threshold))
