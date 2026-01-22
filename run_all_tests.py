#!/usr/bin/env python3
"""
Test Runner for Python DevOps Homework
Runs all 10 task solutions and displays results
"""

import subprocess
import os
import sys
from pathlib import Path

# Set UTF-8 encoding for Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def run_solution(task_number, task_name):
    """Run a single solution and display results"""
    task_dir = f"Task_{task_number:02d}_{task_name}"
    solution_file = f"solution_{task_number:02d}.py"
    solution_path = Path(task_dir) / solution_file
    
    print(f"\n{'='*70}")
    print(f"Task {task_number}: {task_name.replace('_', ' ')}")
    print(f"{'='*70}")
    
    if not solution_path.exists():
        print(f"[X] Solution file not found: {solution_path}")
        return False
    
    try:
        result = subprocess.run(
            ["python", solution_file],
            cwd=task_dir,
            capture_output=True,
            text=True,
            timeout=5,
            encoding='utf-8',
            errors='replace'
        )
        
        if result.returncode == 0:
            print(f"[OK] Success!")
            print(f"\nOutput:")
            print(result.stdout)
            return True
        else:
            print(f"[FAIL] Failed with return code: {result.returncode}")
            if result.stderr:
                print(f"Error: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"[TIMEOUT] Solution took too long to execute")
        return False
    except Exception as e:
        print(f"[ERROR] Error running solution: {e}")
        return False

def main():
    """Run all solutions"""
    print("Python DevOps Homework - Test Runner")
    print("="*70)
    
    tasks = [
        (1, "Domain_Extractor"),
        (2, "Safe_Name_Sanitizer"),
        (3, "Port_Validator"),
        (4, "Fleet_Inventory"),
        (5, "Cloud_Config_Mapper"),
        (6, "Log_File_Duplicator"),
        (7, "Prod_Guard"),
        (8, "Threshold_Alert"),
        (9, "Path_Builder"),
        (10, "Secret_Masker")
    ]
    
    results = []
    for task_num, task_name in tasks:
        success = run_solution(task_num, task_name)
        results.append((task_num, task_name, success))
    
    # Summary
    print(f"\n{'='*70}")
    print("SUMMARY")
    print(f"{'='*70}")
    
    passed = sum(1 for _, _, success in results if success)
    total = len(results)
    
    for task_num, task_name, success in results:
        status = "[PASS]" if success else "[FAIL]"
        print(f"{status} - Task {task_num:02d}: {task_name.replace('_', ' ')}")
    
    print(f"\n{'='*70}")
    print(f"Results: {passed}/{total} tasks passed")
    print(f"{'='*70}")
    
    if passed == total:
        print("SUCCESS: All tasks completed successfully!")
    else:
        print(f"WARNING: {total - passed} task(s) need attention")


if __name__ == "__main__":
    main()
