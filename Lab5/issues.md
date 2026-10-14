# Lab 5: Static Code Analysis

## Before-fix results
- Pylint score: 5.65/10
- Bandit: 4 findings (2 High, 2 Low)
- Flake8: 4 findings

## Fixes to document
1. Add module and function docstrings.
2. Rename functions and arguments to snake_case.
3. Replace the mutable default dictionary with None.
4. Replace MD5 with an appropriate hashing approach.
5. Remove the unused hardcoded password.
6. Replace os.system with safer subprocess execution.
7. Review random.choice for the intended security requirements.
8. Fix all four Flake8 formatting findings.

## Reflection
Pylint checks code quality, Bandit identifies potential security issues, and Flake8 checks style and formatting. The final reports will be compared with the original reports.

## 5. After-fix Results

- Pylint: 10.00/10.
- Bandit: No issues identified.
- Flake8: No style violations reported.
- Python compilation: Successful.
- Program execution: Successful; student scores and class average
  remain unchanged.

## 6. Final Conclusion

The program was improved using static analysis tools. Pylint
confirmed improved code quality, Bandit reported no remaining
issues, and Flake8 reported no formatting violations. The program
was tested after the changes to verify that the demo still works.
