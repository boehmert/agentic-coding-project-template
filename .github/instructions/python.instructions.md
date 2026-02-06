---
name: Python Coding Standards
description: Python coding conventions and best practices.
applyTo: "**/*.py"
---

# Python Coding Standards

These standards apply to all Python files in this workspace.

---

## 1. Module Header (Mandatory)

Every Python file must start with a structured docstring:

```python
"""
Module: package.subpackage.module_name
Workorder: WO01 (or "N/A" for infrastructure)
Purpose: Brief description of what this module does.

Dependencies:
    - external_lib: Used for X
    - internal.module: Provides Y

Inputs:
    - Describe what this module consumes (files, APIs, parameters)

Outputs:
    - Describe what this module produces (files, return values, side effects)

Key Functions/Classes:
    - ClassName: Brief description
    - function_name: Brief description

Tests: tests/unit/test_module_name.py
"""
```

---

## 2. Code Style

### PEP 8 Compliance
- Follow PEP 8 strictly
- Use 4 spaces for indentation (never tabs)
- Maximum line length: 88 characters (Black formatter default)
- Use blank lines to separate logical sections

### Naming Conventions
```python
# Classes: PascalCase
class DataProcessor:
    pass

# Functions and variables: snake_case
def process_data(input_file: str) -> dict:
    result_count = 0

# Constants: UPPER_SNAKE_CASE
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30

# Private members: leading underscore
def _internal_helper():
    pass

# Module-level "constants" that are configuration
config_path = Path("config.yaml")  # lowercase OK if mutable
```

---

## 3. Type Hints (Mandatory)

All functions must have type hints:

```python
from typing import Optional, List, Dict, Union
from pathlib import Path

def load_data(
    file_path: Path,
    encoding: str = "utf-8",
    validate: bool = True
) -> Dict[str, List[str]]:
    """Load and parse data from file."""
    ...

def find_item(items: List[str], key: str) -> Optional[str]:
    """Find item by key, returns None if not found."""
    ...
```

### Complex Types
```python
from typing import TypedDict, Literal

class WorkorderStatus(TypedDict):
    id: str
    status: Literal["PLANNED", "IN_PROGRESS", "DONE"]
    priority: int

def update_status(wo: WorkorderStatus) -> WorkorderStatus:
    ...
```

---

## 4. Docstrings (PEP 257)

Use Google-style docstrings:

```python
def calculate_score(
    values: List[float],
    weights: Optional[List[float]] = None,
    normalize: bool = True
) -> float:
    """Calculate weighted score from values.
    
    Computes a weighted average of the input values. If no weights
    are provided, uses equal weights for all values.
    
    Args:
        values: List of numeric values to score.
        weights: Optional weights for each value. Must match length
            of values if provided.
        normalize: If True, normalize result to 0-1 range.
    
    Returns:
        The calculated score as a float.
    
    Raises:
        ValueError: If weights length doesn't match values length.
        ValueError: If values list is empty.
    
    Example:
        >>> calculate_score([1.0, 2.0, 3.0])
        2.0
        >>> calculate_score([1.0, 2.0], weights=[0.3, 0.7])
        1.7
    """
```

---

## 5. Error Handling

### Be Explicit About Failures
```python
# Bad: Silent failure
def get_config(key: str) -> Optional[str]:
    return config.get(key)  # Returns None silently

# Good: Explicit handling
def get_config(key: str, required: bool = True) -> Optional[str]:
    """Get configuration value by key.
    
    Args:
        key: Configuration key to look up.
        required: If True, raise error when key not found.
    
    Returns:
        Configuration value or None if not required and not found.
    
    Raises:
        KeyError: If required=True and key not found.
    """
    value = config.get(key)
    if value is None and required:
        raise KeyError(f"Required config key not found: {key}")
    return value
```

### Use Custom Exceptions
```python
class WorkorderError(Exception):
    """Base exception for Workorder-related errors."""
    pass

class WorkorderNotFoundError(WorkorderError):
    """Raised when a Workorder cannot be found."""
    def __init__(self, wo_id: str):
        self.wo_id = wo_id
        super().__init__(f"Workorder not found: {wo_id}")
```

---

## 6. Imports

### Order (PEP 8)
```python
# 1. Standard library
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional

# 2. Third-party packages
import pandas as pd
from pydantic import BaseModel

# 3. Local application imports
from .models import Workorder
from .utils import load_config
```

### Absolute vs Relative
- Use **absolute imports** for top-level modules
- Use **relative imports** within a package

---

## 7. Logging

### Use Structured Logging
```python
import logging

logger = logging.getLogger(__name__)

def process_workorder(wo_id: str) -> None:
    logger.info("Processing workorder", extra={"wo_id": wo_id})
    try:
        # ... processing
        logger.info("Workorder completed", extra={"wo_id": wo_id, "status": "success"})
    except Exception as e:
        logger.error(
            "Workorder failed",
            extra={"wo_id": wo_id, "error": str(e)},
            exc_info=True
        )
        raise
```

### Log Levels
- `DEBUG`: Detailed diagnostic information
- `INFO`: Confirmation of expected behavior
- `WARNING`: Unexpected but recoverable situations
- `ERROR`: Failures that prevent a specific operation
- `CRITICAL`: System-wide failures

---

## 8. Testing

### Test File Structure
```python
"""
Tests for module_name.
Workorder: WO01
"""
import pytest
from package.module_name import function_to_test

class TestFunctionName:
    """Tests for function_name."""
    
    def test_happy_path(self):
        """Test normal operation with valid input."""
        result = function_to_test("valid_input")
        assert result == expected_output
    
    def test_edge_case_empty_input(self):
        """Test behavior with empty input."""
        result = function_to_test("")
        assert result is None
    
    def test_error_case_invalid_input(self):
        """Test that invalid input raises appropriate error."""
        with pytest.raises(ValueError, match="Invalid input"):
            function_to_test("invalid")
```

### Naming Conventions
- Test files: `test_<module_name>.py`
- Test classes: `Test<ClassName>` or `Test<FunctionName>`
- Test methods: `test_<scenario>` or `test_<condition>_<expected_result>`

---

## 9. Configuration

### Never Hardcode
```python
# Bad
API_URL = "https://api.example.com"
MAX_RETRIES = 3

# Good
import os
from pathlib import Path

API_URL = os.environ.get("API_URL", "https://api.example.com")
MAX_RETRIES = int(os.environ.get("MAX_RETRIES", "3"))

# Better: Use a config module
from .config import settings
API_URL = settings.api_url
```

### Use .env Files
```python
from dotenv import load_dotenv
load_dotenv()  # Load .env file

# Access via os.environ
api_key = os.environ["API_KEY"]  # Fails loudly if missing
```

---

## 10. Code Comments

### When to Comment
- **Why**, not what (the code shows what)
- Complex algorithms or business logic
- Workarounds for known issues
- TODOs with context

```python
# Good: Explains why
# Using insertion sort here because the list is nearly sorted
# and insertion sort performs O(n) in this case vs O(n log n) for quicksort
for item in items:
    insert_sorted(result, item)

# Good: Documents a workaround
# WORKAROUND: API returns dates as strings in inconsistent formats
# See: https://github.com/example/issue/123
date = parse_flexible_date(response["date"])

# Good: TODO with context
# TODO(WO05): Replace with proper caching once Redis is available
cached_value = simple_memory_cache.get(key)
```

### When NOT to Comment
```python
# Bad: States the obvious
# Increment counter by one
counter += 1

# Bad: Outdated/misleading
# Returns user name  (but actually returns full user object)
return get_user(user_id)
```
