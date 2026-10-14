# Lab 5: Static Code Analysis

## Objective
To improve Python code quality, security, and formatting using
Pylint, Bandit, and Flake8.

## Issues Identified and Fixes

| Issue | Tool | Fix Applied |
|---|---|---|
| Hardcoded password | Bandit B105 | Removed the unused hardcoded credential |
| Weak MD5 hash | Bandit B324 | Replaced MD5 with SHA-256 for answer comparison |
| Non-cryptographic random selection | Bandit B311 | Used secrets.choice for bonus-question selection |
| Shell command execution | Bandit B605 | Removed the unused remote shell execution helper |
| Mutable default argument | Pylint | Changed the default dictionary to None and initialized it inside the function |
| Missing documentation | Pylint | Added module and function docstrings |
| Naming violations | Pylint | Changed function and argument names to snake_case |
| Code-quality issues | Pylint | Used enumerate and simplified conditional statements |
| Formatting violations | Flake8 | Fixed spacing, blank lines, comments, and line length |

## Final Results

- Pylint: 10.00/10
- Bandit: No issues identified
- Flake8: No violations reported
- Python compilation: Successful
- Program execution: Successful

## Reflection

### 1. What is static code analysis?
Static code analysis examines source code without executing it
to identify potential bugs, security issues, and style violations.

### 2. What is the difference between Pylint, Bandit, and Flake8?
Pylint checks code quality, Bandit identifies common security
problems, and Flake8 checks coding style and common errors.

### 3. Why is static analysis important?
It helps identify problems early, improve maintainability,
and reduce security risks.

### 4. What challenges did you face?
Some warnings required understanding the underlying issue and
changing the implementation instead of simply suppressing warnings.

### 5. What did you learn?
I learned how to run static analysis tools, interpret their reports,
fix code issues, and verify changes using before-and-after reports.
