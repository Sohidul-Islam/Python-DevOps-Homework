# DevOps Python Homework: The Automation Specialist

This repository contains 10 Python tasks designed to build fundamental DevOps automation skills.

## 📁 Project Structure

```
Python-DevOps-Homework/
├── Task_01_Domain_Extractor/
│   ├── Problem_01.txt
│   └── solution_01.py
├── Task_02_Safe_Name_Sanitizer/
│   ├── Problem_02.txt
│   └── solution_02.py
├── Task_03_Port_Validator/
│   ├── Problem_03.txt
│   └── solution_03.py
├── Task_04_Fleet_Inventory/
│   ├── Problem_04.txt
│   └── solution_04.py
├── Task_05_Cloud_Config_Mapper/
│   ├── Problem_05.txt
│   └── solution_05.py
├── Task_06_Log_File_Duplicator/
│   ├── Problem_06.txt
│   └── solution_06.py
├── Task_07_Prod_Guard/
│   ├── Problem_07.txt
│   └── solution_07.py
├── Task_08_Threshold_Alert/
│   ├── Problem_08.txt
│   └── solution_08.py
├── Task_09_Path_Builder/
│   ├── Problem_09.txt
│   └── solution_09.py
└── Task_10_Secret_Masker/
    ├── Problem_10.txt
    └── solution_10.py
```

## 🎯 Tasks Overview

### Task 1: The Domain Extractor
**Skills:** String slicing, `.split()` method  
**DevOps Value:** Parsing logs to identify external service calls  
Extract domain names from URLs using string manipulation.

### Task 2: The "Safe Name" Sanitizer
**Skills:** String methods (`.strip()`, `.replace()`, `.lower()`)  
**DevOps Value:** Standardizing resource names in Terraform/Cloud scripts  
Sanitize bucket names for cloud provider compatibility.

### Task 3: The Port Validator
**Skills:** Type conversion, conditionals, integer validation  
**DevOps Value:** Input validation for automation tools  
Validate port numbers for firewall configurations.

### Task 4: The Fleet Inventory
**Skills:** List slicing, indexing  
**DevOps Value:** Managing infrastructure subsets  
Extract specific servers from fleet inventories.

### Task 5: The Cloud Config Mapper
**Skills:** Dictionary manipulation  
**DevOps Value:** Working with JSON responses from cloud APIs  
Manage VM configurations using dictionaries.

### Task 6: The Log File Duplicator
**Skills:** `os` module, `shutil` module, file operations  
**DevOps Value:** Generating mock data for testing pipelines  
Create multiple copies of log files for testing.

### Task 7: The "Prod" Guard
**Skills:** Booleans, conditionals, environment checks  
**DevOps Value:** Implementing safety gates in CI/CD pipelines  
Prevent destructive operations in production environments.

### Task 8: The Threshold Alert
**Skills:** Float formatting, f-strings  
**DevOps Value:** Creating human-readable alerts for Slack/Email  
Format monitoring metrics as percentage alerts.

### Task 9: The Path Builder
**Skills:** `os.path.join`, `pathlib` module  
**DevOps Value:** Cross-platform compatibility  
Build file paths that work on both Windows and Linux.

### Task 10: The Secret Masker
**Skills:** String slicing, masking sensitive data  
**DevOps Value:** Security and compliance in logging  
Mask API keys and secrets in log output.

## 🚀 Running the Solutions

Each task can be run independently:

```bash
# Navigate to a task folder
cd Task_01_Domain_Extractor

# Run the solution
python solution_01.py
```

Or run all solutions at once:

```bash
# From the Python-DevOps-Homework directory
python Task_01_Domain_Extractor/solution_01.py
python Task_02_Safe_Name_Sanitizer/solution_02.py
python Task_03_Port_Validator/solution_03.py
python Task_04_Fleet_Inventory/solution_04.py
python Task_05_Cloud_Config_Mapper/solution_05.py
python Task_06_Log_File_Duplicator/solution_06.py
python Task_07_Prod_Guard/solution_07.py
python Task_08_Threshold_Alert/solution_08.py
python Task_09_Path_Builder/solution_09.py
python Task_10_Secret_Masker/solution_10.py
```

## 📚 Learning Objectives

By completing these tasks, you will learn:
- String manipulation and parsing
- Type conversion and validation
- List and dictionary operations
- File system operations
- Cross-platform compatibility
- Security best practices
- DevOps automation patterns

## 🛠️ Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## 📝 Notes

Each solution includes:
- Clear comments explaining the approach
- Multiple implementation methods where applicable
- Bonus examples demonstrating advanced concepts
- Real-world DevOps use cases

## 🎓 Next Steps

After completing these tasks, consider:
1. Modifying solutions to handle edge cases
2. Combining multiple tasks into larger automation scripts
3. Adding error handling and logging
4. Creating unit tests for each solution
5. Integrating with real DevOps tools (Docker, Kubernetes, Terraform)

---

**Happy Learning! 🚀**
